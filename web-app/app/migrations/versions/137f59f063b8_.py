"""empty message

Revision ID: 137f59f063b8
Revises: 
Create Date: 2018-12-14 22:06:10.211437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '137f59f063b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('device_no', sa.Integer(), nullable=True),
    sa.Column('device_test_no', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('devices')
    # ### end Alembic commands ###
