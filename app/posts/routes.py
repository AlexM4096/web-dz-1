from flask import render_template
from sqlalchemy import desc
from app.posts import bp
from app.models.post import Post

@bp.route('/')
def index():
    posts = Post.query.order_by(desc(Post.create_time)).all()
    return render_template('posts/index.html', posts=posts)

@bp.route('/<string:slug>')
def post(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('posts/post.html', post=post)