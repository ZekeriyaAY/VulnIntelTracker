"""VUln id disabled

Revision ID: 0ce8f559b5b5
Revises: 756e12937a8e
Create Date: 2023-12-30 01:44:08.284335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ce8f559b5b5'
down_revision = '756e12937a8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Vulnerability', schema=None) as batch_op:
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Vulnerability', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), nullable=False))

    # ### end Alembic commands ###