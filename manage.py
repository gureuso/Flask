# -*- coding: utf-8 -*-
import unittest2
from flask import Flask
from flask_script import Manager

from apps.common.database import db_session
from apps.common.response import error
from apps.controllers.index.controllers import app as index_app
from apps.controllers.test.controllers import app as test_app
from config import Config

activate_this = '{0}/venv/bin/activate_this.py'.format(Config.ROOT_DIR)
execfile(activate_this, dict(__file__=activate_this))

app = Flask(__name__)
app.config.from_object(Config.fromAppMode())
app.register_blueprint(index_app, url_prefix='/')
app.register_blueprint(test_app, url_prefix='/test')

application = app


@app.errorhandler(403)
def forbidden(err):
    return error(40300)


@app.errorhandler(404)
def page_not_found(err):
    return error(40400)


@app.errorhandler(410)
def gone(err):
    return error(41000)


@app.errorhandler(500)
def internal_server_error(err):
    return error(50000)


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

# command
manager = Manager(app, with_default_commands=False)


@manager.command
def test():
    """test code"""
    loader = unittest2.TestLoader()
    start_dir = '{0}/apps'.format(Config.ROOT_DIR)
    suite = loader.discover(start_dir)

    runner = unittest2.TextTestRunner()
    runner.run(suite)


@manager.command
def runserver():
    """run flask server"""
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)

if __name__ == "__main__":
    manager.run()