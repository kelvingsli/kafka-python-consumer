"""fix(db):change db table name

Revision ID: 341a83dfdc56
Revises: 
Create Date: 2025-07-07 18:01:22.692831

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '341a83dfdc56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kafka_users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kafka_users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('key_id', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('title_url', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('source', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('kafka_users_pkey'))
    )
    # ### end Alembic commands ###
