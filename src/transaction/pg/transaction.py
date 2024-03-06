from contextlib import contextmanager
from typing import Iterator

from psycopg2._psycopg import connection

from src.transaction.interface import TxAndConnManagerProtocol


class PgTxAndConnManager(TxAndConnManagerProtocol):
    def __init__(self, conn: connection):
        self._conn = conn

    @contextmanager
    def transaction(self) -> Iterator[connection]:
        conn = self._conn
        try:
            yield conn
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()

    def connect(self) -> connection:
        return self._conn
