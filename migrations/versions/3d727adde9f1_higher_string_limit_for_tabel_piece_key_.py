"""higher string limit for tabel Piece, key:quote

Revision ID: 3d727adde9f1
Revises: 11eb397428a2
Create Date: 2023-04-12 15:16:01.565197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d727adde9f1'
down_revision = '11eb397428a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('piece', schema=None) as batch_op:
        batch_op.alter_column('quote',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=400),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('piece', schema=None) as batch_op:
        batch_op.alter_column('quote',
               existing_type=sa.String(length=400),
               type_=sa.VARCHAR(length=80),
               existing_nullable=True)

    # ### end Alembic commands ###