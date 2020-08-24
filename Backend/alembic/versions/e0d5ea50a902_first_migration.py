"""First migration

Revision ID: e0d5ea50a902
Revises: 
Create Date: 2020-08-24 18:42:28.973655

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e0d5ea50a902'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answers',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('public_key', sa.String(), nullable=True),
    sa.Column('private_key', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('votes',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('person_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['answers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    op.drop_table('answers')
    # ### end Alembic commands ###
