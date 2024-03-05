from contextlib import contextmanager

import psycopg2

from src.config.config import PGSettings


@contextmanager
def postgresql_connect(settings: PGSettings):
    conn = psycopg2.connect(
        host=settings.pg_host,
        port=settings.pg_port,
        dbname=settings.postgres_db,
        user=settings.postgres_user,
        password=settings.postgres_password,
    )
    yield conn
    conn.close()
