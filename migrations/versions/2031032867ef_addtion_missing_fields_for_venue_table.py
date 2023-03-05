"""addtion missing fields for Venue table

Revision ID: 2031032867ef
Revises: 643a6d827b51
Create Date: 2023-03-05 15:34:53.183752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2031032867ef'
down_revision = '643a6d827b51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
        batch_op.add_column(sa.Column('website', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('seeking_talent', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('seeking_description', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.drop_column('seeking_description')
        batch_op.drop_column('seeking_talent')
        batch_op.drop_column('website')
        batch_op.drop_column('genres')

    # ### end Alembic commands ###