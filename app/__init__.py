import os

from .routes import auth, eresource, help, home, peerchat   # will use to create files
from . import db
from flask import Flask

 

   
def create_app(test_config = None):
    # create and configure the app
    # __name__ is name of the current python module that is __init__
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'app.sqlite'),  # not sure with file path

    )

    if test_config is None:
        # overrides the default configuration with values taken from config.py
        app.config.from_pyfile('config.py', silent = True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    

    db.init_app(app)        # to initialize db run flask --app app init-db
    app.register_blueprint(auth.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(help.bp)
    app.register_blueprint(peerchat.bp)
    app.register_blueprint(eresource.bp)
    # peerchat.app = app
    

    peerchat.socketio.init_app(app)

    app.add_url_rule('/', endpoint='home')


    return app


app = create_app()


if __name__ == '__main__':
    app = create_app()
    peerchat.socketio.run(app)


# running the app -      flask --app app run --debug