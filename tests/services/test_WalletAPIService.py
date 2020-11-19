# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from unittest import TestCase

from mock import Mock, patch
from pyxmlib.pyxmlib import bin2hstr, hstr2bin

from xm.core.misc import logger
from xm.core.AddressState import AddressState
from xm.daemon.walletd import WalletD
from xm.generated import xmwallet_pb2, xm_pb2
from xm.services.WalletAPIService import WalletAPIService
from tests.misc.helper import get_alice_xmss, get_bob_xmss, set_xm_dir, replacement_getTime

logger.initialize_default()


@patch('xm.core.misc.ntp.getTime', new=replacement_getTime)
class TestWalletAPI(TestCase):
    def __init__(self, *args, **kwargs):
        self.passphrase = '你好'
        self.qaddress = "Q010400ff39df1ba4d1d5b8753e6d04c51c34b95b01fc3650c10ca7b296a18bdc105412c59d0b3b"
        self.hex_seed = "0104008441d43524996f76236141d16b7b324323abf796e77ad" \
                        "7c874622a82f5744bb803f9b404d25733d0db82be7ac6f3c4cf"
        self.mnemonic = "absorb drank lute brick cure evil inept group grey " \
                        "breed hood reefy eager depict weed image law legacy " \
                        "jockey calm lover freeze fact lively wide dread spiral " \
                        "jaguar span rinse salty pulsar violet fare"
        super(TestWalletAPI, self).__init__(*args, **kwargs)

    def test_addNewAddress(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)
            resp = service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)
            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.address[0], 'Q')

    def test_addNewAddressWithSlaves(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            service = WalletAPIService(walletd)
            resp = service.AddNewAddressWithSlaves(xmwallet_pb2.AddNewAddressWithSlavesReq(), context=None)
            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.address[0], 'Q')

    def test_addAddressFromSeed(self):
        with set_xm_dir("wallet_ver1"):
            qaddress = "Q010400ff39df1ba4d1d5b8753e6d04c51c34b95b01fc3650c10ca7b296a18bdc105412c59d0b3b"
            hex_seed = "0104008441d43524996f76236141d16b7b324323abf796e77ad7c874622a82f5744bb803f9b404d25733d0db82be7ac6f3c4cf"

            walletd = WalletD()
            service = WalletAPIService(walletd)
            resp = service.AddAddressFromSeed(xmwallet_pb2.AddAddressFromSeedReq(seed=hex_seed), context=None)
            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.address, qaddress)

    def test_addAddressFromSeed2(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)
            resp = service.AddAddressFromSeed(xmwallet_pb2.AddAddressFromSeedReq(seed=self.mnemonic), context=None)
            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.address, self.qaddress)

    def test_listAddresses(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            resp = service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)
            address = resp.address

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.addresses[0], address)

    def test_removeAddress(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            resp = service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)
            address = resp.address

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(len(resp.addresses), 1)

            resp = service.RemoveAddress(xmwallet_pb2.RemoveAddressReq(address=address), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(len(resp.addresses), 0)

    def test_isValidAddress(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            qaddress = "Q010400ff39df1ba4d1d5b8753e6d04c51c34b95b01fc3650c10ca7b296a18bdc105412c59d0b3b"
            resp = service.IsValidAddress(xmwallet_pb2.ValidAddressReq(address=qaddress), context=None)
            self.assertEqual(resp.valid, "True")

            qaddress = "Q010400ff39df1ba4d1d5b8753e6d04c51c34b95b01fc3650c10ca7b296a18bdc105412c59d0b00"
            resp = service.IsValidAddress(xmwallet_pb2.ValidAddressReq(address=qaddress), context=None)
            self.assertEqual(resp.valid, "False")

    def test_getRecoverySeeds(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            service.AddAddressFromSeed(xmwallet_pb2.AddAddressFromSeedReq(seed=self.mnemonic), context=None)
            resp = service.GetRecoverySeeds(xmwallet_pb2.GetRecoverySeedsReq(address=self.qaddress), context=None)

            self.assertEqual(resp.hexseed, self.hex_seed)
            self.assertEqual(resp.mnemonic, self.mnemonic)

    def test_getWalletInfo(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            resp = service.GetWalletInfo(xmwallet_pb2.GetWalletInfoReq(), context=None)

            self.assertEqual(resp.version, 1)
            self.assertEqual(resp.address_count, 0)
            self.assertFalse(resp.is_encrypted)

    def test_relayTransferTxn(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            resp = service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))
            walletd._public_stub.IsSlave = Mock(
                return_value=xm_pb2.IsSlaveResp(result=True))
            walletd._public_stub.GetOTS = Mock(
                return_value=xm_pb2.GetOTSResp(next_unused_ots_index=0,
                                                unused_ots_index_found=True))

            alice_xmss = get_alice_xmss(4)
            bob_xmss = get_bob_xmss(4)
            qaddresses_to = [alice_xmss.qaddress, bob_xmss.qaddress]
            amounts = [1000000000, 1000000000]

            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            resp = service.RelayTransferTxn(xmwallet_pb2.RelayTransferTxnReq(addresses_to=qaddresses_to,
                                                                              amounts=amounts,
                                                                              fee=100000000,
                                                                              master_address=None,
                                                                              signer_address=qaddress,
                                                                              ots_index=0), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)

    def test_relayTransferTxnBySlave(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            service = WalletAPIService(walletd)

            resp = service.AddNewAddressWithSlaves(xmwallet_pb2.AddNewAddressWithSlavesReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            slaves = walletd.get_slave_list(qaddress)

            addr_state.add_slave_pks_access_type(bytes(hstr2bin(slaves[0][0].pk)), 0)
            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))

            alice_xmss = get_alice_xmss(4)
            bob_xmss = get_bob_xmss(4)
            qaddresses_to = [alice_xmss.qaddress, bob_xmss.qaddress]
            amounts = [1000000000, 1000000000]

            resp = service.RelayTransferTxnBySlave(
                xmwallet_pb2.RelayTransferTxnBySlaveReq(addresses_to=qaddresses_to,
                                                         amounts=amounts,
                                                         fee=100000000,
                                                         master_address=qaddress), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)

    def test_relayMessageTxn(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            service = WalletAPIService(walletd)

            resp = service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))
            walletd._public_stub.GetOTS = Mock(
                return_value=xm_pb2.GetOTSResp(next_unused_ots_index=0,
                                                unused_ots_index_found=True))

            resp = service.RelayMessageTxn(xmwallet_pb2.RelayMessageTxnReq(message=b'Hello xm!',
                                                                            fee=100000000,
                                                                            master_address=None,
                                                                            signer_address=qaddress,
                                                                            ots_index=0), context=None)

            self.assertEqual(0, resp.code)
            self.assertIsNotNone(resp.tx)

    def test_relayMessageTxnBySlave(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            service = WalletAPIService(walletd)

            resp = service.AddNewAddressWithSlaves(xmwallet_pb2.AddNewAddressWithSlavesReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            slaves = walletd.get_slave_list(qaddress)

            addr_state.add_slave_pks_access_type(bytes(hstr2bin(slaves[0][0].pk)), 0)

            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))

            resp = service.RelayMessageTxnBySlave(
                xmwallet_pb2.RelayMessageTxnReq(message=b'Hello xm!',
                                                 fee=100000000,
                                                 master_address=qaddress), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)

    def test_relayTokenTxn(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            resp = service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))
            walletd._public_stub.IsSlave = Mock(
                return_value=xm_pb2.IsSlaveResp(result=True))
            walletd._public_stub.GetOTS = Mock(
                return_value=xm_pb2.GetOTSResp(next_unused_ots_index=0,
                                                unused_ots_index_found=True))

            alice_xmss = get_alice_xmss(4)
            bob_xmss = get_bob_xmss(4)
            qaddresses = [alice_xmss.qaddress, bob_xmss.qaddress]
            amounts = [1000000000, 1000000000]

            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            resp = service.RelayTokenTxn(xmwallet_pb2.RelayTokenTxnReq(symbol=b'xm',
                                                                        name=b'Quantum Resistant Ledger',
                                                                        owner=alice_xmss.qaddress,
                                                                        decimals=5,
                                                                        addresses=qaddresses,
                                                                        amounts=amounts,
                                                                        fee=100000000,
                                                                        master_address=None,
                                                                        signer_address=qaddress,
                                                                        ots_index=0), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)

    def test_relayTokenTxnBySlave(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            service = WalletAPIService(walletd)

            resp = service.AddNewAddressWithSlaves(xmwallet_pb2.AddNewAddressWithSlavesReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            slaves = walletd.get_slave_list(qaddress)

            addr_state.add_slave_pks_access_type(bytes(hstr2bin(slaves[0][0].pk)), 0)
            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))

            alice_xmss = get_alice_xmss(4)
            bob_xmss = get_bob_xmss(4)
            qaddresses = [alice_xmss.qaddress, bob_xmss.qaddress]
            amounts = [1000000000, 1000000000]

            resp = service.RelayTokenTxnBySlave(
                xmwallet_pb2.RelayTokenTxnBySlaveReq(symbol=b'xm',
                                                      name=b'Quantum Resistant Ledger',
                                                      owner=alice_xmss.qaddress,
                                                      decimals=5,
                                                      addresses=qaddresses,
                                                      amounts=amounts,
                                                      fee=100000000,
                                                      master_address=qaddress), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)

    def test_relayTransferTokenTxn(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            resp = service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))
            walletd._public_stub.IsSlave = Mock(
                return_value=xm_pb2.IsSlaveResp(result=True))
            walletd._public_stub.GetOTS = Mock(
                return_value=xm_pb2.GetOTSResp(next_unused_ots_index=0,
                                                unused_ots_index_found=True))

            alice_xmss = get_alice_xmss(4)
            bob_xmss = get_bob_xmss(4)
            qaddresses_to = [alice_xmss.qaddress, bob_xmss.qaddress]
            amounts = [1000000000, 1000000000]

            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            resp = service.RelayTransferTokenTxn(xmwallet_pb2.RelayTransferTokenTxnReq(addresses_to=qaddresses_to,
                                                                                        amounts=amounts,
                                                                                        token_txhash='',
                                                                                        fee=100000000,
                                                                                        master_address=None,
                                                                                        signer_address=qaddress,
                                                                                        ots_index=0), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)

    def test_relayTransferTokenTxnBySlave(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            service = WalletAPIService(walletd)

            resp = service.AddNewAddressWithSlaves(xmwallet_pb2.AddNewAddressWithSlavesReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            slaves = walletd.get_slave_list(qaddress)

            addr_state.add_slave_pks_access_type(bytes(hstr2bin(slaves[0][0].pk)), 0)
            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))

            alice_xmss = get_alice_xmss(4)
            bob_xmss = get_bob_xmss(4)
            qaddresses_to = [alice_xmss.qaddress, bob_xmss.qaddress]
            amounts = [1000000000, 1000000000]

            resp = service.RelayTransferTokenTxnBySlave(
                xmwallet_pb2.RelayTransferTokenTxnBySlaveReq(addresses_to=qaddresses_to,
                                                              amounts=amounts,
                                                              token_txhash='',
                                                              fee=100000000,
                                                              master_address=qaddress), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)

    def test_relaySlaveTxn(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            resp = service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))
            walletd._public_stub.IsSlave = Mock(
                return_value=xm_pb2.IsSlaveResp(result=True))
            walletd._public_stub.GetOTS = Mock(
                return_value=xm_pb2.GetOTSResp(next_unused_ots_index=0,
                                                unused_ots_index_found=True))

            alice_xmss = get_alice_xmss(4)
            slave_pks = [alice_xmss.pk]
            access_types = [0]

            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            resp = service.RelaySlaveTxn(xmwallet_pb2.RelaySlaveTxnReq(slave_pks=slave_pks,
                                                                        access_types=access_types,
                                                                        fee=100000000,
                                                                        master_address=None,
                                                                        signer_address=qaddress,
                                                                        ots_index=0), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)

    def test_relaySlaveTxnBySlave(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            walletd._public_stub.PushTransaction = Mock(
                return_value=xm_pb2.PushTransactionResp(error_code=xm_pb2.PushTransactionResp.SUBMITTED))

            service = WalletAPIService(walletd)

            resp = service.AddNewAddressWithSlaves(xmwallet_pb2.AddNewAddressWithSlavesReq(), context=None)
            qaddress = resp.address
            addr_state = AddressState.get_default(walletd.qaddress_to_address(qaddress))
            slaves = walletd.get_slave_list(qaddress)

            addr_state.add_slave_pks_access_type(bytes(hstr2bin(slaves[0][0].pk)), 0)
            walletd._public_stub.GetAddressState = Mock(
                return_value=xm_pb2.GetAddressStateResp(state=addr_state.pbdata))

            alice_xmss = get_alice_xmss(4)
            slave_pks = [alice_xmss.pk]
            access_types = [0]

            resp = service.RelaySlaveTxnBySlave(
                xmwallet_pb2.RelaySlaveTxnBySlaveReq(slave_pks=slave_pks,
                                                      access_types=access_types,
                                                      fee=100000000,
                                                      master_address=qaddress), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)

    def test_encryptWallet(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)

            resp = service.EncryptWallet(xmwallet_pb2.EncryptWalletReq(), context=None)
            self.assertEqual(resp.code, 1)

            resp = service.EncryptWallet(xmwallet_pb2.EncryptWalletReq(passphrase=self.passphrase), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.EncryptWallet(xmwallet_pb2.EncryptWalletReq(passphrase=self.passphrase), context=None)
            self.assertEqual(resp.code, 1)

    def test_lockWallet(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 0)
            self.assertEqual(len(resp.addresses), 1)

            resp = service.EncryptWallet(xmwallet_pb2.EncryptWalletReq(passphrase=self.passphrase), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 1)

            resp = service.UnlockWallet(xmwallet_pb2.UnlockWalletReq(passphrase=self.passphrase), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.LockWallet(xmwallet_pb2.LockWalletReq(), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 1)

    def test_unlockWallet(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 0)
            self.assertEqual(len(resp.addresses), 1)

            resp = service.EncryptWallet(xmwallet_pb2.EncryptWalletReq(passphrase=self.passphrase), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 1)

            resp = service.UnlockWallet(xmwallet_pb2.UnlockWalletReq(passphrase=self.passphrase), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.LockWallet(xmwallet_pb2.LockWalletReq(), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 1)

            resp = service.UnlockWallet(xmwallet_pb2.UnlockWalletReq(), context=None)
            self.assertEqual(resp.code, 1)

            resp = service.UnlockWallet(xmwallet_pb2.UnlockWalletReq(passphrase="wrong"), context=None)
            self.assertEqual(resp.code, 1)

    def test_changePassphrase(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            service.AddNewAddress(xmwallet_pb2.AddNewAddressReq(), context=None)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 0)
            self.assertEqual(len(resp.addresses), 1)

            resp = service.EncryptWallet(xmwallet_pb2.EncryptWalletReq(passphrase=self.passphrase), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 1)

            resp = service.UnlockWallet(xmwallet_pb2.UnlockWalletReq(passphrase=self.passphrase), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.ListAddresses(xmwallet_pb2.ListAddressesReq(), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.LockWallet(xmwallet_pb2.LockWalletReq(), context=None)
            self.assertEqual(resp.code, 0)

            new_passphrase = "Hello World"
            resp = service.ChangePassphrase(
                xmwallet_pb2.ChangePassphraseReq(oldPassphrase=self.passphrase,
                                                  newPassphrase=new_passphrase), context=None)
            self.assertEqual(resp.code, 0)

            resp = service.UnlockWallet(xmwallet_pb2.UnlockWalletReq(passphrase=self.passphrase), context=None)
            self.assertEqual(resp.code, 1)

            resp = service.UnlockWallet(xmwallet_pb2.UnlockWalletReq(passphrase=new_passphrase), context=None)
            self.assertEqual(resp.code, 0)

    def test_getTransactionsByAddress(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            walletd._public_stub.GetMiniTransactionsByAddress = Mock(
                return_value=xm_pb2.GetMiniTransactionsByAddressResp(mini_transactions=[],
                                                                      balance=0))

            resp = service.GetTransactionsByAddress(
                xmwallet_pb2.TransactionsByAddressReq(address=get_alice_xmss(4).qaddress), context=None)

            self.assertEqual(resp.code, 0)
            self.assertEqual(len(resp.mini_transactions), 0)
            self.assertEqual(resp.balance, 0)

    def test_getTransaction(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            tx = xm_pb2.Transaction()
            tx.fee = 10
            tx.transaction_hash = b'1234'
            tx.message.message_hash = b'hello'
            pk = '01020016ecb9f39b9f4275d5a49e232346a15ae2fa8c50a2927daeac189b8c5f2d1' \
                 '8bc4e3983bd564298c49ae2e7fa6e28d4b954d8cd59398f1225b08d6144854aee0e'
            tx.public_key = bytes(hstr2bin(pk))

            walletd._public_stub.GetTransaction = Mock(
                return_value=xm_pb2.GetTransactionResp(tx=tx, confirmations=10))

            resp = service.GetTransaction(xmwallet_pb2.TransactionReq(tx_hash=tx.transaction_hash), context=None)

            self.assertEqual(resp.code, 0)
            self.assertIsNotNone(resp.tx)
            self.assertEqual(resp.tx.transaction_hash, bin2hstr(tx.transaction_hash))
            self.assertEqual(resp.confirmations, "10")

    def test_getBalance(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            walletd._public_stub.GetBalance = Mock(
                return_value=xm_pb2.GetBalanceResp(balance=1000))

            resp = service.GetBalance(xmwallet_pb2.BalanceReq(address=self.qaddress), context=None)

            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.balance, "1000")

    def test_getTotalBalance(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            walletd._public_stub.GetTotalBalance = Mock(
                return_value=xm_pb2.GetTotalBalanceResp(balance=6000))

            resp = service.GetTotalBalance(xmwallet_pb2.TotalBalanceReq(), context=None)

            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.balance, "6000")

    def test_getOTS(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            ots_bitfield_by_page = xm_pb2.OTSBitfieldByPage(ots_bitfield=[b'\x00'] * 10,
                                                             page_number=1)
            walletd._public_stub.GetOTS = Mock(
                return_value=xm_pb2.GetOTSResp(ots_bitfield_by_page=[ots_bitfield_by_page],
                                                next_unused_ots_index=1,
                                                unused_ots_index_found=True))

            resp = service.GetOTS(xmwallet_pb2.OTSReq(address=self.qaddress), context=None)
            self.assertEqual(resp.code, 0)
            self.assertEqual(len(resp.ots_bitfield_by_page), 1)
            self.assertEqual(resp.ots_bitfield_by_page[0], ots_bitfield_by_page)
            self.assertEqual(resp.next_unused_ots_index, 1)

    def test_getHeight(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            walletd._public_stub.GetHeight = Mock(
                return_value=xm_pb2.GetHeightResp(height=1001))

            resp = service.GetHeight(xmwallet_pb2.HeightReq(), context=None)

            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.height, 1001)

    def test_getBlock(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            block = xm_pb2.Block()
            block.header.hash_header = b'001122'
            block.header.block_number = 1

            walletd._public_stub.GetBlock = Mock(
                return_value=xm_pb2.GetBlockResp(block=block))

            resp = service.GetBlock(xmwallet_pb2.BlockReq(header_hash=b'001122'), context=None)

            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.block.header.hash_header, bin2hstr(block.header.hash_header))
            self.assertEqual(resp.block.header.block_number, block.header.block_number)

    def test_getBlockByNumber(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            block = xm_pb2.Block()
            block.header.hash_header = b'001122'
            block.header.block_number = 1

            walletd._public_stub.GetBlockByNumber = Mock(
                return_value=xm_pb2.GetBlockResp(block=block))

            resp = service.GetBlockByNumber(xmwallet_pb2.BlockByNumberReq(block_number=1), context=None)

            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.block.header.hash_header, bin2hstr(block.header.hash_header))
            self.assertEqual(resp.block.header.block_number, block.header.block_number)

    def test_getAddressFromPK(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            pk = '01020016ecb9f39b9f4275d5a49e232346a15ae2fa8c50a2927daeac189b8c5f2d1' \
                 '8bc4e3983bd564298c49ae2e7fa6e28d4b954d8cd59398f1225b08d6144854aee0e'

            resp = service.GetAddressFromPK(xmwallet_pb2.AddressFromPKReq(pk=pk), context=None)

            self.assertEqual(resp.code, 0)
            self.assertEqual(resp.address,
                             'Q010200670246b0026436b717f199e3ec5320ba6ab61d5eddff811ac199a9e9b871d3280178b343')

    def test_getNodeInfo(self):
        with set_xm_dir("wallet_ver1"):
            walletd = WalletD()
            service = WalletAPIService(walletd)

            block_last_hash_str = 'c23f47a10a8c53cc5ded096369255a32c4a218682a961d0ee7db22c500000000'

            version = "1.0.0"
            num_connections = 10
            num_known_peers = 200
            uptime = 10000
            block_height = 102345
            block_last_hash = bytes(hstr2bin(block_last_hash_str))
            network_id = "network id"
            node_info = xm_pb2.NodeInfo(version=version,
                                         num_connections=num_connections,
                                         num_known_peers=num_known_peers,
                                         uptime=uptime,
                                         block_height=block_height,
                                         block_last_hash=block_last_hash,
                                         network_id=network_id)
            walletd._public_stub.GetNodeState = Mock(
                return_value=xm_pb2.GetNodeStateResp(info=node_info))

            resp = service.GetNodeInfo(xmwallet_pb2.NodeInfoReq(), context=None)

            self.assertEqual(resp.version, version)
            self.assertEqual(resp.num_connections, str(num_connections))
            self.assertEqual(resp.num_known_peers, str(num_known_peers))
            self.assertEqual(resp.uptime, uptime)
            self.assertEqual(resp.block_height, block_height)
            self.assertEqual(resp.block_last_hash, block_last_hash_str)
            self.assertEqual(resp.network_id, network_id)
