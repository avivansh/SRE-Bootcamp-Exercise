"""add phone number column

Revision ID: d14f3c172265
Revises: beab566ed9a7
Create Date: 2024-03-04 00:02:19.232279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd14f3c172265'
down_revision: Union[str, None] = 'beab566ed9a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('students',
    sa.Column('phone_number', sa.String())
    )
    pass


def downgrade() -> None:
    op.drop_column("students", "phone_number")
    pass
