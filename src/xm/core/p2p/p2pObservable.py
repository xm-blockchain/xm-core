from xm.core.notification.Observable import Observable
from xm.generated import xmlegacy_pb2


class P2PObservable(Observable):
    def __init__(self, source):
        # FIXME: Add mutexes
        super().__init__(source)

    def notify(self, message: xmlegacy_pb2.LegacyMessage):
        # TODO: Add some p2p specific validation?
        super().notify(message)
