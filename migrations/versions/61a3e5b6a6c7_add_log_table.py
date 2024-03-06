"""add_log_table

Revision ID: 61a3e5b6a6c7
Revises: 27c5cda8f287
Create Date: 2024-03-06 21:18:23.996205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61a3e5b6a6c7'
down_revision: Union[str, None] = '27c5cda8f287'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

CITY_LOG_TABLE = "city_log"


def upgrade() -> None:
    op.create_table(
        CITY_LOG_TABLE,
        sa.Column("id", sa.BIGINT, primary_key=True),
        sa.Column("city_name", sa.TEXT, unique=True, nullable=False),
        sa.Column("count_requests", sa.BIGINT),
    )


def downgrade() -> None:
    op.drop_table(CITY_LOG_TABLE)
