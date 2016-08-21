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
    
    
    
    
    














def listen_for_tweets()
    pass




# inside def homepage():

q = Queue(connection=Redis())
result = q.enqueue(listen_for_tweets)
tweets = session.query(Tweet).all()
return render_template("homepage.html")

