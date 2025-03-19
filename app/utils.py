from faker import Faker
from app.extensions import db 
from app.models.post import Post

fake = Faker()

def generate_fake_posts(num_posts, is_new=False):
    for _ in range(num_posts):
        create_time = (
            fake.date_time_between(start_date='-3d', end_date='now') if is_new 
            else fake.date_time_this_decade()
        ).replace(tzinfo=None)

        post = Post(
            title=fake.sentence(nb_words=6),
            content=fake.text(),
            create_time=create_time
        )

        db.session.add(post)

    db.session.commit()

def clear_db():
    db.drop_all()
    db.create_all()