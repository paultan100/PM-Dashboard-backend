"""empty message

Revision ID: 386880d225cd
Revises: 7c9ec763c45f
Create Date: 2020-09-10 10:39:55.443228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '386880d225cd'
down_revision = '7c9ec763c45f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('capability', sa.Column('dependency', sa.String(), 
                  nullable=False, server_default='N/A'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('capability', 'dependency')
    # ### end Alembic commands ###
