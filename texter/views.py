from flask import render_template
from flask import request, redirect, url_for
from . import app
from .database import session
from flask import flash
from flask.ext.login import login_user
from werkzeug.security import check_password_hash
from .database import User, Notification
from flask.ext.login import login_required
from flask.ext.login import current_user

@app.route("/")
def home():
    return render_template("base.html")
    
@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    email = request.form["email"]
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect username or password", "danger")
        return redirect(url_for("login_get"))

    login_user(user)
    return redirect(request.args.get('next') or url_for("dashboard"))
  
@app.route("/dashboard")
@login_required
def dashboard():
    notifications = session.query(Notification).all()
    return render_template("dashboard.html",notifications=notifications)
    
@app.route("/notification/new")
@login_required
def new_notification():
    return render_template("new_notification.html")
    
@app.route("/notification/new", methods=["POST"])
@login_required
def new_notification_post():
    subject = request.form["subject"]
    timezone = request.form["timezone"]
    frequency = request.form["frequency"]
    days = request.form["days"]
    status = request.form["status"]
    user = session.query(User).first()
    notification = Notification(
        subject = subject,
        timezone = timezone,
        frequency = frequency,
        days = days,
        status = status,
        user = user)
    session.add(notification)
    session.commit()
    #call twilio function here
    #enable or disable
    return redirect(url_for("dashboard"))
    
    
@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")
    
@app.route("/notification/<id>/edit")
@login_required
def edit_notification(id):
    notification = session.query(Notification)
    notification = notification.get(id)
    return render_template("edit_notification.html", notification = notification)
    #left side, notif variable on html file. right side, notif of query

@app.route("/notification/<id>/edit", methods=["POST"])
@login_required
def edit_notification_post(id):
    notification = session.query(Notification)
    notification = notification.get(id)
    notification.subject = request.form["subject"]
    notification.timezone = request.form["timezone"]
    notification.frequency = request.form["frequency"]
    notification.days = request.form["days"]
    notification.status = request.form["status"]
    session.commit()
    return redirect(url_for("dashboard"))
