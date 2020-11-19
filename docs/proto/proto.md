# Protocol Documentation
<a name="top"/>

## Table of Contents

- [xm.proto](#xm.proto)
    - [AddressList](#xm.AddressList)
    - [AddressState](#xm.AddressState)
    - [Block](#xm.Block)
    - [BlockExtended](#xm.BlockExtended)
    - [BlockHeader](#xm.BlockHeader)
    - [BlockHeaderExtended](#xm.BlockHeaderExtended)
    - [BlockMetaData](#xm.BlockMetaData)
    - [BlockMetaDataList](#xm.BlockMetaDataList)
    - [EphemeralMessage](#xm.EphemeralMessage)
    - [GenesisBalance](#xm.GenesisBalance)
    - [GetAddressStateReq](#xm.GetAddressStateReq)
    - [GetAddressStateResp](#xm.GetAddressStateResp)
    - [GetBlockReq](#xm.GetBlockReq)
    - [GetBlockResp](#xm.GetBlockResp)
    - [GetKnownPeersReq](#xm.GetKnownPeersReq)
    - [GetKnownPeersResp](#xm.GetKnownPeersResp)
    - [GetLatestDataReq](#xm.GetLatestDataReq)
    - [GetLatestDataResp](#xm.GetLatestDataResp)
    - [GetLocalAddressesReq](#xm.GetLocalAddressesReq)
    - [GetLocalAddressesResp](#xm.GetLocalAddressesResp)
    - [GetNodeStateReq](#xm.GetNodeStateReq)
    - [GetNodeStateResp](#xm.GetNodeStateResp)
    - [GetObjectReq](#xm.GetObjectReq)
    - [GetObjectResp](#xm.GetObjectResp)
    - [GetStakersReq](#xm.GetStakersReq)
    - [GetStakersResp](#xm.GetStakersResp)
    - [GetStatsReq](#xm.GetStatsReq)
    - [GetStatsResp](#xm.GetStatsResp)
    - [GetWalletReq](#xm.GetWalletReq)
    - [GetWalletResp](#xm.GetWalletResp)
    - [LatticePublicKeyTxnReq](#xm.LatticePublicKeyTxnReq)
    - [MR](#xm.MR)
    - [MsgObject](#xm.MsgObject)
    - [NodeInfo](#xm.NodeInfo)
    - [Peer](#xm.Peer)
    - [PingReq](#xm.PingReq)
    - [PongResp](#xm.PongResp)
    - [PushTransactionReq](#xm.PushTransactionReq)
    - [PushTransactionResp](#xm.PushTransactionResp)
    - [StakeValidator](#xm.StakeValidator)
    - [StakeValidatorsList](#xm.StakeValidatorsList)
    - [StakeValidatorsTracker](#xm.StakeValidatorsTracker)
    - [StakeValidatorsTracker.ExpiryEntry](#xm.StakeValidatorsTracker.ExpiryEntry)
    - [StakeValidatorsTracker.FutureStakeAddressesEntry](#xm.StakeValidatorsTracker.FutureStakeAddressesEntry)
    - [StakeValidatorsTracker.FutureSvDictEntry](#xm.StakeValidatorsTracker.FutureSvDictEntry)
    - [StakeValidatorsTracker.SvDictEntry](#xm.StakeValidatorsTracker.SvDictEntry)
    - [StakerData](#xm.StakerData)
    - [StoredPeers](#xm.StoredPeers)
    - [Timestamp](#xm.Timestamp)
    - [Transaction](#xm.Transaction)
    - [Transaction.CoinBase](#xm.Transaction.CoinBase)
    - [Transaction.Destake](#xm.Transaction.Destake)
    - [Transaction.Duplicate](#xm.Transaction.Duplicate)
    - [Transaction.LatticePublicKey](#xm.Transaction.LatticePublicKey)
    - [Transaction.Stake](#xm.Transaction.Stake)
    - [Transaction.Transfer](#xm.Transaction.Transfer)
    - [Transaction.Vote](#xm.Transaction.Vote)
    - [TransactionCount](#xm.TransactionCount)
    - [TransactionCount.CountEntry](#xm.TransactionCount.CountEntry)
    - [TransactionExtended](#xm.TransactionExtended)
    - [TransferCoinsReq](#xm.TransferCoinsReq)
    - [TransferCoinsResp](#xm.TransferCoinsResp)
    - [Wallet](#xm.Wallet)
    - [WalletStore](#xm.WalletStore)

    - [GetLatestDataReq.Filter](#xm.GetLatestDataReq.Filter)
    - [GetStakersReq.Filter](#xm.GetStakersReq.Filter)
    - [NodeInfo.State](#xm.NodeInfo.State)
    - [Transaction.Type](#xm.Transaction.Type)


    - [AdminAPI](#xm.AdminAPI)
    - [P2PAPI](#xm.P2PAPI)
    - [PublicAPI](#xm.PublicAPI)


- [xmbase.proto](#xmbase.proto)
    - [GetNodeInfoReq](#xm.GetNodeInfoReq)
    - [GetNodeInfoResp](#xm.GetNodeInfoResp)



    - [Base](#xm.Base)


- [xmlegacy.proto](#xmlegacy.proto)
    - [BKData](#xm.BKData)
    - [FBData](#xm.FBData)
    - [LegacyMessage](#xm.LegacyMessage)
    - [MRData](#xm.MRData)
    - [NoData](#xm.NoData)
    - [PBData](#xm.PBData)
    - [PLData](#xm.PLData)
    - [PONGData](#xm.PONGData)
    - [SYNCData](#xm.SYNCData)
    - [VEData](#xm.VEData)

    - [LegacyMessage.FuncName](#xm.LegacyMessage.FuncName)




- [Scalar Value Types](#scalar-value-types)



<a name="xm.proto"/>
<p align="right"><a href="#top">Top</a></p>

## xm.proto



<a name="xm.AddressList"/>

### AddressList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addresses | [bytes](#bytes) | repeated |  |






<a name="xm.AddressState"/>

### AddressState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |
| balance | [uint64](#uint64) |  |  |
| nonce | [uint64](#uint64) |  | FIXME: Discuss. 32 or 64 bits? |
| pubhashes | [bytes](#bytes) | repeated |  |
| transaction_hashes | [bytes](#bytes) | repeated |  |






<a name="xm.Block"/>

### Block



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#xm.BlockHeader) |  |  |
| transactions | [Transaction](#xm.Transaction) | repeated |  |
| dup_transactions | [Transaction](#xm.Transaction) | repeated | TODO: Review this |
| vote | [Transaction](#xm.Transaction) | repeated |  |
| genesis_balance | [GenesisBalance](#xm.GenesisBalance) | repeated | This is only applicable to genesis blocks |






<a name="xm.BlockExtended"/>

### BlockExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block | [Block](#xm.Block) |  |  |
| voted_weight | [uint64](#uint64) |  |  |
| total_stake_weight | [uint64](#uint64) |  |  |






<a name="xm.BlockHeader"/>

### BlockHeader



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  | Header |
| epoch | [uint64](#uint64) |  |  |
| timestamp | [Timestamp](#xm.Timestamp) |  | FIXME: Temporary |
| hash_header | [bytes](#bytes) |  |  |
| hash_header_prev | [bytes](#bytes) |  |  |
| reward_block | [uint64](#uint64) |  |  |
| reward_fee | [uint64](#uint64) |  |  |
| merkle_root | [bytes](#bytes) |  |  |
| hash_reveal | [bytes](#bytes) |  |  |
| stake_selector | [bytes](#bytes) |  |  |






<a name="xm.BlockHeaderExtended"/>

### BlockHeaderExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#xm.BlockHeader) |  |  |
| transaction_count | [TransactionCount](#xm.TransactionCount) |  |  |
| voted_weight | [uint64](#uint64) |  |  |
| total_stake_weight | [uint64](#uint64) |  |  |






<a name="xm.BlockMetaData"/>

### BlockMetaData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| hash_header | [bytes](#bytes) |  |  |






<a name="xm.BlockMetaDataList"/>

### BlockMetaDataList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number_hashes | [BlockMetaData](#xm.BlockMetaData) | repeated |  |






<a name="xm.EphemeralMessage"/>

### EphemeralMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [bytes](#bytes) |  |  |
| ttl | [uint64](#uint64) |  |  |
| data | [bytes](#bytes) |  | Encrypted String containing aes256_symkey, prf512_seed, xmss_address, signature |






<a name="xm.EphemeralMessage.Data"/>

### EphemeralMessage.Data



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| aes256_symkey | [bytes](#bytes) |  |  |
| prf512_seed | [bytes](#bytes) |  |  |
| xmss_address | [bytes](#bytes) |  |  |
| xmss_signature | [bytes](#bytes) |  |  |






<a name="xm.GenesisBalance"/>

### GenesisBalance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [string](#string) |  | Address is string only here to increase visibility |
| balance | [uint64](#uint64) |  |  |






<a name="xm.GetAddressStateReq"/>

### GetAddressStateReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |






<a name="xm.GetAddressStateResp"/>

### GetAddressStateResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [AddressState](#xm.AddressState) |  |  |






<a name="xm.GetBlockReq"/>

### GetBlockReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  | Indicates the index number in mainchain |
| after_hash | [bytes](#bytes) |  | request the node that comes after hash |






<a name="xm.GetBlockResp"/>

### GetBlockResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#xm.NodeInfo) |  |  |
| block | [Block](#xm.Block) |  |  |






<a name="xm.GetKnownPeersReq"/>

### GetKnownPeersReq







<a name="xm.GetKnownPeersResp"/>

### GetKnownPeersResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#xm.NodeInfo) |  |  |
| known_peers | [Peer](#xm.Peer) | repeated |  |






<a name="xm.GetLatestDataReq"/>

### GetLatestDataReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter | [GetLatestDataReq.Filter](#xm.GetLatestDataReq.Filter) |  |  |
| offset | [uint32](#uint32) |  | Offset in the result list (works backwards in this case) |
| quantity | [uint32](#uint32) |  | Number of items to retrive. Capped at 100 |






<a name="xm.GetLatestDataResp"/>

### GetLatestDataResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| blockheaders | [BlockHeaderExtended](#xm.BlockHeaderExtended) | repeated |  |
| transactions | [TransactionExtended](#xm.TransactionExtended) | repeated |  |
| transactions_unconfirmed | [TransactionExtended](#xm.TransactionExtended) | repeated |  |






<a name="xm.GetLocalAddressesReq"/>

### GetLocalAddressesReq







<a name="xm.GetLocalAddressesResp"/>

### GetLocalAddressesResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addresses | [bytes](#bytes) | repeated |  |






<a name="xm.GetNodeStateReq"/>

### GetNodeStateReq







<a name="xm.GetNodeStateResp"/>

### GetNodeStateResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| info | [NodeInfo](#xm.NodeInfo) |  |  |






<a name="xm.GetObjectReq"/>

### GetObjectReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query | [bytes](#bytes) |  |  |






<a name="xm.GetObjectResp"/>

### GetObjectResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| found | [bool](#bool) |  |  |
| address_state | [AddressState](#xm.AddressState) |  |  |
| transaction | [TransactionExtended](#xm.TransactionExtended) |  |  |
| block | [Block](#xm.Block) |  |  |






<a name="xm.GetStakersReq"/>

### GetStakersReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter | [GetStakersReq.Filter](#xm.GetStakersReq.Filter) |  | Indicates which group of stakers (current / next) |
| offset | [uint32](#uint32) |  | Offset in the staker list |
| quantity | [uint32](#uint32) |  | Number of stakers to retrive. Capped at 100 |






<a name="xm.GetStakersResp"/>

### GetStakersResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stakers | [StakerData](#xm.StakerData) | repeated |  |






<a name="xm.GetStatsReq"/>

### GetStatsReq







<a name="xm.GetStatsResp"/>

### GetStatsResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#xm.NodeInfo) |  |  |
| epoch | [uint64](#uint64) |  | Current epoch |
| uptime_network | [uint64](#uint64) |  | Indicates uptime in seconds |
| stakers_count | [uint64](#uint64) |  | Number of active stakers |
| block_last_reward | [uint64](#uint64) |  |  |
| block_time_mean | [uint64](#uint64) |  |  |
| block_time_sd | [uint64](#uint64) |  |  |
| coins_total_supply | [uint64](#uint64) |  |  |
| coins_emitted | [uint64](#uint64) |  |  |
| coins_atstake | [uint64](#uint64) |  |  |






<a name="xm.GetWalletReq"/>

### GetWalletReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |






<a name="xm.GetWalletResp"/>

### GetWalletResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| wallet | [Wallet](#xm.Wallet) |  | FIXME: Encrypt |






<a name="xm.LatticePublicKeyTxnReq"/>

### LatticePublicKeyTxnReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_from | [bytes](#bytes) |  |  |
| kyber_pk | [bytes](#bytes) |  |  |
| dilithium_pk | [bytes](#bytes) |  |  |
| xmss_pk | [bytes](#bytes) |  |  |
| xmss_ots_index | [uint64](#uint64) |  |  |






<a name="xm.MR"/>

### MR
FIXME: This is legacy. Plan removal


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hash | [bytes](#bytes) |  | FIXME: rename this to block_headerhash |
| type | [string](#string) |  | FIXME: type/string what is this |
| stake_selector | [bytes](#bytes) |  |  |
| block_number | [uint64](#uint64) |  |  |
| prev_headerhash | [bytes](#bytes) |  |  |
| reveal_hash | [bytes](#bytes) |  |  |






<a name="xm.MsgObject"/>

### MsgObject



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ephemeral | [EphemeralMessage](#xm.EphemeralMessage) |  | Overlapping - objects used for 2-way exchanges P2PRequest request = 1; P2PResponse response = 2; |






<a name="xm.NodeInfo"/>

### NodeInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| state | [NodeInfo.State](#xm.NodeInfo.State) |  |  |
| num_connections | [uint32](#uint32) |  |  |
| num_known_peers | [uint32](#uint32) |  |  |
| uptime | [uint64](#uint64) |  | Uptime in seconds |
| block_height | [uint64](#uint64) |  |  |
| block_last_hash | [bytes](#bytes) |  |  |
| stake_enabled | [bool](#bool) |  |  |
| network_id | [string](#string) |  |  |






<a name="xm.Peer"/>

### Peer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ip | [string](#string) |  |  |






<a name="xm.PingReq"/>

### PingReq







<a name="xm.PongResp"/>

### PongResp







<a name="xm.PushTransactionReq"/>

### PushTransactionReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transaction_signed | [Transaction](#xm.Transaction) |  |  |






<a name="xm.PushTransactionResp"/>

### PushTransactionResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| some_response | [string](#string) |  |  |






<a name="xm.StakeValidator"/>

### StakeValidator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |
| slave_public_key | [bytes](#bytes) |  |  |
| terminator_hash | [bytes](#bytes) |  |  |
| balance | [uint64](#uint64) |  |  |
| activation_blocknumber | [uint64](#uint64) |  |  |
| nonce | [uint64](#uint64) |  |  |
| is_banned | [bool](#bool) |  |  |
| is_active | [bool](#bool) |  |  |






<a name="xm.StakeValidatorsList"/>

### StakeValidatorsList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stake_validators | [StakeValidator](#xm.StakeValidator) | repeated |  |






<a name="xm.StakeValidatorsTracker"/>

### StakeValidatorsTracker



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sv_dict | [StakeValidatorsTracker.SvDictEntry](#xm.StakeValidatorsTracker.SvDictEntry) | repeated |  |
| future_stake_addresses | [StakeValidatorsTracker.FutureStakeAddressesEntry](#xm.StakeValidatorsTracker.FutureStakeAddressesEntry) | repeated |  |
| expiry | [StakeValidatorsTracker.ExpiryEntry](#xm.StakeValidatorsTracker.ExpiryEntry) | repeated |  |
| future_sv_dict | [StakeValidatorsTracker.FutureSvDictEntry](#xm.StakeValidatorsTracker.FutureSvDictEntry) | repeated |  |
| total_stake_amount | [uint64](#uint64) |  |  |






<a name="xm.StakeValidatorsTracker.ExpiryEntry"/>

### StakeValidatorsTracker.ExpiryEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [AddressList](#xm.AddressList) |  |  |






<a name="xm.StakeValidatorsTracker.FutureStakeAddressesEntry"/>

### StakeValidatorsTracker.FutureStakeAddressesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [StakeValidator](#xm.StakeValidator) |  |  |






<a name="xm.StakeValidatorsTracker.FutureSvDictEntry"/>

### StakeValidatorsTracker.FutureSvDictEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [StakeValidatorsList](#xm.StakeValidatorsList) |  |  |






<a name="xm.StakeValidatorsTracker.SvDictEntry"/>

### StakeValidatorsTracker.SvDictEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [StakeValidator](#xm.StakeValidator) |  |  |






<a name="xm.StakerData"/>

### StakerData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_state | [AddressState](#xm.AddressState) |  |  |
| terminator_hash | [bytes](#bytes) |  |  |






<a name="xm.StoredPeers"/>

### StoredPeers



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| peers | [Peer](#xm.Peer) | repeated |  |






<a name="xm.Timestamp"/>

### Timestamp
TODO: Avoid using timestamp until the github issue is fixed
import &#34;google/protobuf/timestamp.proto&#34;;


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seconds | [int64](#int64) |  |  |
| nanos | [int32](#int32) |  |  |






<a name="xm.Transaction"/>

### Transaction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [Transaction.Type](#xm.Transaction.Type) |  |  |
| nonce | [uint64](#uint64) |  |  |
| addr_from | [bytes](#bytes) |  |  |
| public_key | [bytes](#bytes) |  |  |
| transaction_hash | [bytes](#bytes) |  |  |
| ots_key | [uint32](#uint32) |  |  |
| signature | [bytes](#bytes) |  |  |
| transfer | [Transaction.Transfer](#xm.Transaction.Transfer) |  |  |
| stake | [Transaction.Stake](#xm.Transaction.Stake) |  |  |
| coinbase | [Transaction.CoinBase](#xm.Transaction.CoinBase) |  |  |
| latticePK | [Transaction.LatticePublicKey](#xm.Transaction.LatticePublicKey) |  |  |
| duplicate | [Transaction.Duplicate](#xm.Transaction.Duplicate) |  |  |
| vote | [Transaction.Vote](#xm.Transaction.Vote) |  |  |






<a name="xm.Transaction.CoinBase"/>

### Transaction.CoinBase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addr_to | [bytes](#bytes) |  |  |
| amount | [uint64](#uint64) |  |  |






<a name="xm.Transaction.Destake"/>

### Transaction.Destake







<a name="xm.Transaction.Duplicate"/>

### Transaction.Duplicate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| prev_header_hash | [uint64](#uint64) |  |  |
| coinbase1_hhash | [bytes](#bytes) |  |  |
| coinbase2_hhash | [bytes](#bytes) |  |  |
| coinbase1 | [Transaction](#xm.Transaction) |  |  |
| coinbase2 | [Transaction](#xm.Transaction) |  |  |






<a name="xm.Transaction.LatticePublicKey"/>

### Transaction.LatticePublicKey



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| kyber_pk | [bytes](#bytes) |  |  |
| dilithium_pk | [bytes](#bytes) |  |  |






<a name="xm.Transaction.Stake"/>

### Transaction.Stake



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activation_blocknumber | [uint64](#uint64) |  |  |
| slavePK | [bytes](#bytes) |  |  |
| hash | [bytes](#bytes) |  |  |






<a name="xm.Transaction.Transfer"/>

### Transaction.Transfer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addr_to | [bytes](#bytes) |  |  |
| amount | [uint64](#uint64) |  |  |
| fee | [uint64](#uint64) |  |  |






<a name="xm.Transaction.Vote"/>

### Transaction.Vote



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| hash_header | [bytes](#bytes) |  |  |






<a name="xm.TransactionCount"/>

### TransactionCount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [TransactionCount.CountEntry](#xm.TransactionCount.CountEntry) | repeated |  |






<a name="xm.TransactionCount.CountEntry"/>

### TransactionCount.CountEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="xm.TransactionExtended"/>

### TransactionExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#xm.BlockHeader) |  |  |
| tx | [Transaction](#xm.Transaction) |  |  |






<a name="xm.TransferCoinsReq"/>

### TransferCoinsReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_from | [bytes](#bytes) |  | Transaction source address |
| address_to | [bytes](#bytes) |  | Transaction destination address |
| amount | [uint64](#uint64) |  | Amount. It should be expressed in Shor |
| fee | [uint64](#uint64) |  | Fee. It should be expressed in Shor |
| xmss_pk | [bytes](#bytes) |  | XMSS Public key |
| xmss_ots_index | [uint64](#uint64) |  | XMSS One time signature index |






<a name="xm.TransferCoinsResp"/>

### TransferCoinsResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transaction_unsigned | [Transaction](#xm.Transaction) |  |  |






<a name="xm.Wallet"/>

### Wallet



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [string](#string) |  | FIXME move to bytes |
| mnemonic | [string](#string) |  |  |
| xmss_index | [int32](#int32) |  |  |






<a name="xm.WalletStore"/>

### WalletStore



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| wallets | [Wallet](#xm.Wallet) | repeated |  |








<a name="xm.GetLatestDataReq.Filter"/>

### GetLatestDataReq.Filter


| Name | Number | Description |
| ---- | ------ | ----------- |
| ALL | 0 |  |
| BLOCKHEADERS | 1 |  |
| TRANSACTIONS | 2 |  |
| TRANSACTIONS_UNCONFIRMED | 3 |  |



<a name="xm.GetStakersReq.Filter"/>

### GetStakersReq.Filter


| Name | Number | Description |
| ---- | ------ | ----------- |
| CURRENT | 0 |  |
| NEXT | 1 |  |



<a name="xm.NodeInfo.State"/>

### NodeInfo.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| UNSYNCED | 1 |  |
| SYNCING | 2 |  |
| SYNCED | 3 |  |
| FORKED | 4 |  |



<a name="xm.Transaction.Type"/>

### Transaction.Type


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| TRANSFER | 1 |  |
| STAKE | 2 |  |
| DESTAKE | 3 |  |
| COINBASE | 4 |  |
| LATTICE | 5 |  |
| DUPLICATE | 6 |  |
| VOTE | 7 |  |







<a name="xm.AdminAPI"/>

### AdminAPI
This is a place holder for testing/instrumentation APIs

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetLocalAddresses | [GetLocalAddressesReq](#xm.GetLocalAddressesReq) | [GetLocalAddressesResp](#xm.GetLocalAddressesReq) | FIXME: Use TLS and some signature scheme to validate the cli? At the moment, it will run locally |


<a name="xm.P2PAPI"/>

### P2PAPI
This service describes the P2P API

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeState | [GetNodeStateReq](#xm.GetNodeStateReq) | [GetNodeStateResp](#xm.GetNodeStateReq) |  |
| GetKnownPeers | [GetKnownPeersReq](#xm.GetKnownPeersReq) | [GetKnownPeersResp](#xm.GetKnownPeersReq) |  |
| GetBlock | [GetBlockReq](#xm.GetBlockReq) | [GetBlockResp](#xm.GetBlockReq) | rpc PublishBlock(PublishBlockReq) returns (PublishBlockResp); |
| ObjectExchange | [MsgObject](#xm.MsgObject) | [MsgObject](#xm.MsgObject) | A bidirectional streaming channel is used to avoid any firewalling/NAT issues. |


<a name="xm.PublicAPI"/>

### PublicAPI
This service describes the Public API used by clients (wallet/cli/etc)

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeState | [GetNodeStateReq](#xm.GetNodeStateReq) | [GetNodeStateResp](#xm.GetNodeStateReq) |  |
| GetKnownPeers | [GetKnownPeersReq](#xm.GetKnownPeersReq) | [GetKnownPeersResp](#xm.GetKnownPeersReq) |  |
| GetStats | [GetStatsReq](#xm.GetStatsReq) | [GetStatsResp](#xm.GetStatsReq) |  |
| GetAddressState | [GetAddressStateReq](#xm.GetAddressStateReq) | [GetAddressStateResp](#xm.GetAddressStateReq) |  |
| GetObject | [GetObjectReq](#xm.GetObjectReq) | [GetObjectResp](#xm.GetObjectReq) |  |
| GetLatestData | [GetLatestDataReq](#xm.GetLatestDataReq) | [GetLatestDataResp](#xm.GetLatestDataReq) |  |
| GetStakers | [GetStakersReq](#xm.GetStakersReq) | [GetStakersResp](#xm.GetStakersReq) |  |
| TransferCoins | [TransferCoinsReq](#xm.TransferCoinsReq) | [TransferCoinsResp](#xm.TransferCoinsReq) |  |
| PushTransaction | [PushTransactionReq](#xm.PushTransactionReq) | [PushTransactionResp](#xm.PushTransactionReq) |  |
| GetLatticePublicKeyTxn | [LatticePublicKeyTxnReq](#xm.LatticePublicKeyTxnReq) | [TransferCoinsResp](#xm.LatticePublicKeyTxnReq) |  |





<a name="xmbase.proto"/>
<p align="right"><a href="#top">Top</a></p>

## xmbase.proto



<a name="xm.GetNodeInfoReq"/>

### GetNodeInfoReq







<a name="xm.GetNodeInfoResp"/>

### GetNodeInfoResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| grpcProto | [string](#string) |  |  |












<a name="xm.Base"/>

### Base


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeInfo | [GetNodeInfoReq](#xm.GetNodeInfoReq) | [GetNodeInfoResp](#xm.GetNodeInfoReq) |  |





<a name="xmlegacy.proto"/>
<p align="right"><a href="#top">Top</a></p>

## xmlegacy.proto



<a name="xm.BKData"/>

### BKData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mrData | [MRData](#xm.MRData) |  |  |
| block | [Block](#xm.Block) |  |  |






<a name="xm.FBData"/>

### FBData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  |  |






<a name="xm.LegacyMessage"/>

### LegacyMessage
Adding old code to refactor while keeping things working


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| func_name | [LegacyMessage.FuncName](#xm.LegacyMessage.FuncName) |  |  |
| noData | [NoData](#xm.NoData) |  |  |
| veData | [VEData](#xm.VEData) |  |  |
| pongData | [PONGData](#xm.PONGData) |  |  |
| mrData | [MRData](#xm.MRData) |  |  |
| sfmData | [MRData](#xm.MRData) |  |  |
| bkData | [BKData](#xm.BKData) |  |  |
| fbData | [FBData](#xm.FBData) |  |  |
| pbData | [PBData](#xm.PBData) |  |  |
| pbbData | [PBData](#xm.PBData) |  |  |
| syncData | [SYNCData](#xm.SYNCData) |  |  |






<a name="xm.MRData"/>

### MRData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hash | [bytes](#bytes) |  | FIXME: rename this to block_headerhash |
| type | [LegacyMessage.FuncName](#xm.LegacyMessage.FuncName) |  | FIXME: type/string what is this |
| stake_selector | [bytes](#bytes) |  |  |
| block_number | [uint64](#uint64) |  |  |
| prev_headerhash | [bytes](#bytes) |  |  |
| reveal_hash | [bytes](#bytes) |  |  |






<a name="xm.NoData"/>

### NoData







<a name="xm.PBData"/>

### PBData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  |  |
| block | [Block](#xm.Block) |  |  |






<a name="xm.PLData"/>

### PLData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| peer_ips | [string](#string) | repeated |  |






<a name="xm.PONGData"/>

### PONGData







<a name="xm.SYNCData"/>

### SYNCData







<a name="xm.VEData"/>

### VEData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| genesis_prev_hash | [bytes](#bytes) |  |  |








<a name="xm.LegacyMessage.FuncName"/>

### LegacyMessage.FuncName


| Name | Number | Description |
| ---- | ------ | ----------- |
| VE | 0 | Version |
| PL | 1 | Peers List |
| PONG | 2 | Pong |
| MR | 3 | Message received |
| SFM | 4 | Send Full Message |
| BK | 5 | Block |
| FB | 6 | Fetch request for block |
| PB | 7 | Push Block |
| PBB | 8 | Push Block Buffer |
| ST | 9 | Stake Transaction |
| DST | 10 | Destake Transaction |
| DT | 11 | Duplicate Transaction |
| TX | 12 | Transfer Transaction |
| VT | 13 | Vote |
| SYNC | 14 | Add into synced list, if the node replies |










## Scalar Value Types

| .proto Type | Notes | C++ Type | Java Type | Python Type |
| ----------- | ----- | -------- | --------- | ----------- |
| <a name="double" /> double |  | double | double | float |
| <a name="float" /> float |  | float | float | float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long |
| <a name="bool" /> bool |  | bool | boolean | boolean |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str |

