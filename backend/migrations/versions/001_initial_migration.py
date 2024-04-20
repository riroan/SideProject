"""001_Initial_migration

Revision ID: 893780c71756
Revises:
Create Date: 2024-04-20 11:41:08.378697

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "893780c71756"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("nickname", sa.String(length=100), nullable=False),
        sa.Column("password", sa.String(length=200), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("gender", sa.Integer(), nullable=False),
        sa.Column("birthday", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "code",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("language", sa.String(length=100), nullable=False),
        sa.Column("code", sa.Text(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("code")
    op.drop_table("user")
    # ### end Alembic commands ###
