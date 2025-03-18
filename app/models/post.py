from app.extensions import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Post "{self.title}">'