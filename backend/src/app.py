from flask import Flask
from flask_migrate import Migrate

from src.utils.logger import logger
from src.routes import notification_routes
from src.routes import vcs_routes
from src.routes import gitlab_routes
from src.routes import github_routes
from src.routes import bitbucket_routes
from src.models import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(github_routes.github_bp, url_prefix='/github')
    app.register_blueprint(gitlab_routes.gitlab_bp, url_prefix='/gitlab')
    app.register_blueprint(bitbucket_routes.bitbucket_bp, url_prefix='/bitbucket')
    app.register_blueprint(vcs_routes.vcs_bp, url_prefix='/vcs')
    app.register_blueprint(notification_routes.notification_bp, url_prefix='/notify')

    logger.info('Starting flask app')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
