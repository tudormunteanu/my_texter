import os
from flask.ext.script import Manager
from texter import app
from getpass import getpass
from werkzeug.security import generate_password_hash
from flask.ext.migrate import Migrate, MigrateCommand
from texter.database import Base

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    
class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()