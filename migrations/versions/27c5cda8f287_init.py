"""init

Revision ID: 27c5cda8f287
Revises: 
Create Date: 2024-03-05 19:29:29.027054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27c5cda8f287'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


REQUEST_HISTORY_TABLE = "requests_history"


def upgrade() -> None:
    op.create_table(
        REQUEST_HISTORY_TABLE,
        sa.Column("id", sa.BIGINT, primary_key=True),
        sa.Column("city_name", sa.TEXT),
        sa.Column("weather_conditions", sa.TEXT),
        sa.Column("temperature", sa.FLOAT),
        sa.Column("feels_like", sa.FLOAT),
        sa.Column("wind_speed", sa.FLOAT),
        sa.Column("time", sa.TIMESTAMP),
        sa.Column("timezone", sa.TEXT),
    )


def downgrade() -> None:
    op.drop_table(REQUEST_HISTORY_TABLE)
