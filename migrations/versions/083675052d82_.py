"""empty message

Revision ID: 083675052d82
Revises: 2fd523904a9a
Create Date: 2016-12-17 14:18:59.109016

"""

# revision identifiers, used by Alembic.
revision = '083675052d82'
down_revision = '2fd523904a9a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assignment', sa.Column('text_date', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assignment', 'text_date')
    ### end Alembic commands ###