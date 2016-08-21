import os
from flask.ext.script import Manager
from texter.database import session, User
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

@manager.command
def add_user():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    number = input("Number: ")
    
    if session.query(User).filter_by(email=email).first():
        print("User with that email address already exists")
        return

    #password = ""
    #while len(password) < 8 or password != password_2:
    #    password = getpass("Password: ")
    #    password_2 = getpass("Re-enter password: ")
    user = User(first_name=first_name, last_name=last_name,email=email, number=number,
                password=generate_password_hash(password))
    session.add(user)
    session.commit()    

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
    
    
    
    
    














def listen_for_tweets()
    pass




# inside def homepage():

q = Queue(connection=Redis())
result = q.enqueue(listen_for_tweets)
tweets = session.query(Tweet).all()
return render_template("homepage.html")

