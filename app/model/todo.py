from app import db
from app.model.asocative_table import todo_categories
from datetime import datetime

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    priority = db.Column(db.Enum('low', 'medium', 'high', name='priority_enum'), default='medium')
    deadline = db.Column(db.DateTime, nullable=True)
    is_completed = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relasi Many-to-Many ke Category
    categories = db.relationship(
        'Category',
        secondary=todo_categories,
        back_populates='todos'
    )

    def __repr__(self):
        return f'<Todo {self.title}>'