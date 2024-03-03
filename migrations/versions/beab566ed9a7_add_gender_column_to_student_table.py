"""add gender column to student table

Revision ID: beab566ed9a7
Revises: b9fa3cc012ab
Create Date: 2024-03-03 21:49:34.911727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'beab566ed9a7'
down_revision: Union[str, None] = 'b9fa3cc012ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('students',
    sa.Column('gender', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_column("students", "gender")
    pass
