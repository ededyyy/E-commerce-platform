"""change seller username to brandname, delete seller's first and last name

Revision ID: 3c102bc9cf0f
Revises: 069d7274d81f
Create Date: 2024-12-12 20:06:40.366875

"""
from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c102bc9cf0f'
down_revision = '069d7274d81f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sellers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brandname', sa.String(length=80), nullable=False))
        batch_op.create_unique_constraint('uq_sellers_brandname', ['brandname'])
        batch_op.drop_column('firstname')
        batch_op.drop_column('username')
        if context.get_context().dialect.name != 'sqlite':
            batch_op.drop_column('lastname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sellers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lastname', sa.VARCHAR(length=100), nullable=False))
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=80), nullable=False))
        batch_op.add_column(sa.Column('firstname', sa.VARCHAR(length=100), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('brandname')

    # ### end Alembic commands ###
