"""empty message

Revision ID: 392a1d8727ed
Revises: 
Create Date: 2023-07-27 00:18:23.291712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '392a1d8727ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_User_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_User_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_User_username'))
        batch_op.drop_index(batch_op.f('ix_User_email'))

    op.drop_table('User')
    # ### end Alembic commands ###