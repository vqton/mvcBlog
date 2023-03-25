from app import db
from .user_model import User

class Author(User):
    __tablename__ = 'author'

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    bio = db.Column(db.Text)
    articles = db.relationship('Article', backref='author', lazy=True)

    def __repr__(self):
        return f'<Author {self.name}>'