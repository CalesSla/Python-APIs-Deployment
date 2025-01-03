"""add last few columns to posts table

Revision ID: 37a400e2d74b
Revises: 6641bc45e981
Create Date: 2024-12-27 14:50:36.439210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37a400e2d74b'
down_revision = '6641bc45e981'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
                  sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts",
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
