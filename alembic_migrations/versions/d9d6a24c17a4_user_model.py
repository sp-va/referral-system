"""User model

Revision ID: d9d6a24c17a4
Revises: d46991ae4130
Create Date: 2024-04-09 23:56:26.126913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy


# revision identifiers, used by Alembic.
revision: str = 'd9d6a24c17a4'
down_revision: Union[str, None] = 'd46991ae4130'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(), nullable=False))
    op.add_column('user', sa.Column('referral_code', sa.Uuid(), nullable=False))
    op.add_column('user', sa.Column('parent_referral_code', sa.Uuid(), nullable=False))
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'parent_referral_code')
    op.drop_column('user', 'referral_code')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
