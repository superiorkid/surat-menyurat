"""add relations between user and surat_masuk table

Revision ID: ebe3a3ec4245
Revises: 287bf38591dc
Create Date: 2022-08-24 08:12:07.212698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebe3a3ec4245'
down_revision = '287bf38591dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('surat_masuk', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'surat_masuk', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'surat_masuk', type_='foreignkey')
    op.drop_column('surat_masuk', 'user_id')
    # ### end Alembic commands ###
