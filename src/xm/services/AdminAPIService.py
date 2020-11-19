# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.

from xm.core.xmnode import xmNode
from xm.generated.xm_pb2_grpc import AdminAPIServicer


class AdminAPIService(AdminAPIServicer):
    # TODO: Separate the Service from the node model
    def __init__(self, xmnode: xmNode):
        self.xmnode = xmnode
