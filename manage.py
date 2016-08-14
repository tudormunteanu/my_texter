import os
from flask.ext.script import Manager
from texter import app
from getpass import getpass
from werkzeug.security import generate_password_hash


manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    manager.run()