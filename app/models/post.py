from app.extensions import db
from datetime import datetime, timedelta
from app.slug import HasSlug

class Post(db.Model, HasSlug):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now())

    @property
    def is_new(self):
        return datetime.now() - self.create_time < timedelta(days=3)

    def __repr__(self):
        return f'<Post "{self.title}">'