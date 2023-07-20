from flask import Flask
from .views import index, vuln


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    app.register_blueprint(index.bp)
    app.register_blueprint(vuln.bp)

    return app
