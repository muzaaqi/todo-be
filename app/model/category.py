from app import db
from app.model.asocative_table import todo_categories
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relasi Many-to-Many
    todos = db.relationship(
        'Todo',
        secondary=todo_categories,
        back_populates='categories'
    )

    def __repr__(self):
        return f'<Category {self.name}>'