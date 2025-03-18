from flask import Flask
from flask_bootstrap import Bootstrap5

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap = Bootstrap5(app)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.forms import bp as form_bp
    app.register_blueprint(form_bp, url_prefix='/forms')

    return app