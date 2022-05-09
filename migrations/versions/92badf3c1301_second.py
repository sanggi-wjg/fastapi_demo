"""second

Revision ID: 92badf3c1301
Revises: 0a7b6c1099ce
Create Date: 2022-05-09 11:42:29.119152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92badf3c1301'
down_revision = '0a7b6c1099ce'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key = True, autoincrement = True, index = True),
        sa.Column('user_email', sa.String(length = 50), unique = True, nullable = False, index = True),
        sa.Column('user_hashed_password', sa.String(length = 250), nullable = False),
        sa.Column('is_active', sa.Boolean, default = True)
    )

    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key = True, autoincrement = True, index = True),
        sa.Column('item_name', sa.String(length = 100), nullable = False, index = True),
        sa.Column('item_description', sa.String(length = 250), index = True),
        sa.Column('item_price', sa.Numeric(10, 2)),
        sa.Column('item_tax', sa.Numeric(10, 2)),

        sa.Column('owner_id', sa.Integer, nullable = False),
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('items')
