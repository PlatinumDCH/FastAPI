"""upgrade

Revision ID: 552fbcc0dc3b
Revises: 05b1de1d37e8
Create Date: 2024-12-06 13:13:58.556447

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '552fbcc0dc3b'
down_revision: Union[str, None] = '05b1de1d37e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""
    DO $$
    BEGIN
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'role') THEN
            CREATE TYPE role AS ENUM('admin', 'moderator', 'user');
        END IF;
    END
    $$;
    """)
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('DROP TYPE role')
    pass
    # ### end Alembic commands ###