# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from grpc import StatusCode

from pyxmlib.pyxmlib import bin2hstr

from xm.core import config
from xm.core.xmnode import xmNode
from xm.crypto.Qryptonight import Qryptonight
from xm.generated import xmmining_pb2
from xm.generated.xmmining_pb2_grpc import MiningAPIServicer
from xm.services.grpcHelper import GrpcExceptionWrapper


class MiningAPIService(MiningAPIServicer):
    MAX_REQUEST_QUANTITY = 100

    def __init__(self, xmnode: xmNode):
        self.xmnode = xmnode
        self._qn = Qryptonight()

    @GrpcExceptionWrapper(xmmining_pb2.GetBlockMiningCompatibleResp, StatusCode.UNKNOWN)
    def GetBlockMiningCompatible(self,
                                 request: xmmining_pb2.GetBlockMiningCompatibleReq,
                                 context) -> xmmining_pb2.GetBlockMiningCompatibleResp:

        blockheader, block_metadata = self.xmnode.get_blockheader_and_metadata(request.height)

        response = xmmining_pb2.GetBlockMiningCompatibleResp()
        if blockheader is not None and block_metadata is not None:
            response = xmmining_pb2.GetBlockMiningCompatibleResp(
                blockheader=blockheader.pbdata,
                blockmetadata=block_metadata.pbdata)

        return response

    @GrpcExceptionWrapper(xmmining_pb2.GetLastBlockHeaderResp, StatusCode.UNKNOWN)
    def GetLastBlockHeader(self,
                           request: xmmining_pb2.GetLastBlockHeaderReq,
                           context) -> xmmining_pb2.GetLastBlockHeaderResp:
        response = xmmining_pb2.GetLastBlockHeaderResp()

        blockheader, block_metadata = self.xmnode.get_blockheader_and_metadata(request.height)

        response.difficulty = int(bin2hstr(block_metadata.block_difficulty), 16)
        response.height = blockheader.block_number
        response.timestamp = blockheader.timestamp
        response.reward = blockheader.block_reward + blockheader.fee_reward
        response.hash = bin2hstr(blockheader.headerhash)
        response.depth = self.xmnode.block_height - blockheader.block_number

        return response

    @GrpcExceptionWrapper(xmmining_pb2.GetBlockToMineResp, StatusCode.UNKNOWN)
    def GetBlockToMine(self,
                       request: xmmining_pb2.GetBlockToMineReq,
                       context) -> xmmining_pb2.GetBlockToMineResp:

        response = xmmining_pb2.GetBlockToMineResp()

        blocktemplate_blob_and_difficulty = self.xmnode.get_block_to_mine(request.wallet_address)

        if blocktemplate_blob_and_difficulty:
            response.blocktemplate_blob = blocktemplate_blob_and_difficulty[0]
            response.difficulty = blocktemplate_blob_and_difficulty[1]
            response.height = self.xmnode.block_height + 1
            response.reserved_offset = config.dev.extra_nonce_offset
            seed_block_number = self._qn.get_seed_height(response.height)
            response.seed_hash = bin2hstr(self.xmnode.get_block_header_hash_by_number(seed_block_number))

        return response

    @GrpcExceptionWrapper(xmmining_pb2.GetBlockToMineResp, StatusCode.UNKNOWN)
    def SubmitMinedBlock(self,
                         request: xmmining_pb2.SubmitMinedBlockReq,
                         context) -> xmmining_pb2.SubmitMinedBlockResp:
        response = xmmining_pb2.SubmitMinedBlockResp()

        response.error = not self.xmnode.submit_mined_block(request.blob)

        return response
