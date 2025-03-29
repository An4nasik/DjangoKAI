import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class Celebrity(SqlAlchemyBase):
    __tablename__ = 'celebrities'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(100), nullable=False)
    bio = sa.Column(sa.Text)
    birth_date = sa.Column(sa.Date)
    profession = sa.Column(sa.String(100))
    photo_url = sa.Column(sa.String(255))
    is_published = sa.Column(sa.Boolean, default=True)

    def __repr__(self):
        return f"<Celebrity {self.id}: {self.name}>"