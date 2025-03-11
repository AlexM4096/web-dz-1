from flask import render_template
from app.posts import bp
from app.extensions import db
from app.models.post import Post

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

@bp.route('/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/post.html', post=post)