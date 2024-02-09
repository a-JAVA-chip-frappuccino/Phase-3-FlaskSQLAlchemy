"""empty message

Revision ID: b9b1ed3f9b5d
Revises: 4e5bb498b74d
Create Date: 2024-02-09 13:57:54.605520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9b1ed3f9b5d'
down_revision = '4e5bb498b74d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeroom_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('students', 'classes', ['homeroom_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('homeroom_id')

    # ### end Alembic commands ###