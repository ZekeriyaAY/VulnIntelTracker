from flask import Flask
from flask_migrate import Migrate
from .views import index, vuln
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(index.bp)
    app.register_blueprint(vuln.bp)

    return app
