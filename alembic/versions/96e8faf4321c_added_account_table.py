"""Added account table

Revision ID: 96e8faf4321c
Revises: 7e2786d7e34b
Create Date: 2022-04-26 15:44:25.120531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96e8faf4321c'
down_revision = '7e2786d7e34b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student_subject', 'diem4')
    op.drop_column('student_subject', 'diem2')
    op.drop_column('student_subject', 'diem1')
    op.drop_column('student_subject', 'diem3')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student_subject', sa.Column('diem3', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('student_subject', sa.Column('diem1', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('student_subject', sa.Column('diem2', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('student_subject', sa.Column('diem4', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
