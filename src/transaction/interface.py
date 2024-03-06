from contextlib import contextmanager
from typing import Protocol


class TxAndConnManagerProtocol(Protocol):

    @contextmanager
    def transaction(self):
        pass

    def connect(self):
        pass