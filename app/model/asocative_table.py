from app import db

todo_categories = db.Table(
    'todo_categories',
    db.Column('todo_id', db.Integer, db.ForeignKey('todos.id', ondelete='CASCADE'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), primary_key=True)
)