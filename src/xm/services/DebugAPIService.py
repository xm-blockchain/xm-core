# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from xm.core import config
from xm.core.xmnode import xmNode
from xm.generated import xmdebug_pb2
from xm.generated.xmdebug_pb2_grpc import DebugAPIServicer
from xm.services.grpcHelper import GrpcExceptionWrapper


class DebugAPIService(DebugAPIServicer):
    MAX_REQUEST_QUANTITY = 100

    def __init__(self, xmnode: xmNode):
        self.xmnode = xmnode

    @GrpcExceptionWrapper(xmdebug_pb2.GetFullStateResp)
    def GetFullState(self, request: xmdebug_pb2.GetFullStateReq, context) -> xmdebug_pb2.GetFullStateResp:
        return xmdebug_pb2.GetFullStateResp(
            coinbase_state=self.xmnode.get_address_state(config.dev.coinbase_address).pbdata,
            addresses_state=self.xmnode.get_all_address_state()
        )
