from app import db
from datetime import datetime

todo_categories = db.Table(
    'todo_categories',
    db.Column('todo_id', db.Integer, db.ForeignKey('todos.id', ondelete='CASCADE'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), primary_key=True)
)

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