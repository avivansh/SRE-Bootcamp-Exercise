"""add temp column

Revision ID: 66b74fddb2c1
Revises: d14f3c172265
Create Date: 2024-03-04 00:35:46.160983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66b74fddb2c1'
down_revision: Union[str, None] = 'd14f3c172265'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('students',
    sa.Column('temp', sa.String())
    )
    pass


def downgrade() -> None:
    op.drop_column("students", "temp")
    pass
