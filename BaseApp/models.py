# BaseApp/models.py
import sqlalchemy as sa
from datetime import date
from .db_session import SqlAlchemyBase


class Star(SqlAlchemyBase):
    __tablename__ = 'stars'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(100), nullable=False)
    bio = sa.Column(sa.Text, nullable=True)
    birth_date = sa.Column(sa.Date, nullable=False)
    profession = sa.Column(sa.String(100), nullable=False)
    country = sa.Column(sa.String(100), nullable=True)
    photo_url = sa.Column(sa.String(255), nullable=True)
    publish = sa.Column(sa.Boolean, default=True)

    def __repr__(self):
        return f"<Star {self.id}: {self.name}>"