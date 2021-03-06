"""url, user and artist tables

Revision ID: 031e0a59f2d6
Revises: 
Create Date: 2018-04-30 19:35:10.100634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '031e0a59f2d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('genres', sa.String(length=140), nullable=True),
    sa.Column('born', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_artist_name'), 'artist', ['name'], unique=False)
    op.create_table('url',
    sa.Column('url', sa.String(length=140), nullable=False),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('url')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_table('url')
    op.drop_index(op.f('ix_artist_name'), table_name='artist')
    op.drop_table('artist')
    # ### end Alembic commands ###
