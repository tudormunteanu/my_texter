from flask import render_template
from flask import request, redirect, url_for
from . import app
from .database import session
from flask import flash
from flask.ext.login import login_user
from werkzeug.security import check_password_hash
from .database import User
from flask.ext.login import login_required
from flask.ext.login import current_user

@app.route("/")
def home():
    return render_template("base.html")
