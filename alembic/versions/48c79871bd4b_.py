"""Adding User table, removing default MyModel table

Revision ID: 48c79871bd4b
Revises: 670424a6e5
Create Date: 2012-04-07 10:23:54.211717

"""

# revision identifiers, used by Alembic.
revision = '48c79871bd4b'
down_revision = '670424a6e5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Unicode(length=32), nullable=True),
    sa.Column('email', sa.Unicode(length=256), nullable=True),
    sa.Column('name', sa.Unicode(length=60), nullable=True),
    sa.Column('password', sa.Unicode(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table(u'models')

def downgrade():
    op.create_table(u'models',
    sa.Column(u'id', sa.INTEGER(), primary_key=True, nullable=False),
    sa.Column(u'name', sa.TEXT(), nullable=True),
    sa.Column(u'value', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint(u'id', name=u'models_pkey')
    )
    op.drop_table('users')
