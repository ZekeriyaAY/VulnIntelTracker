from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from config import Config
import logging
from logging.handlers import RotatingFileHandler
import os


db = SQLAlchemy()
migrate = Migrate()
moment = Moment()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)  # initialize database
    migrate.init_app(app, db)  # initialize migration engine
    moment.init_app(app)  # initialize moment.js

    from .main import bp as main_bp
    from .errors import bp as errors_bp
    from .vulnerability import bp as vulnerability_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(vulnerability_bp)

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/trackerapp.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)  # log only INFO and below

        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('TrackerApp startup')

    return app
