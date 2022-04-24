"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import request, jsonify, send_file
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from app.models import User, Car, Favourite
from app.forms import LoginForm, RegisterForm, CarForm, SearchForm
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
import os
import datetime 
import jwt
import json

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###
@app.route('/api/register', methods=['POST'])
def register():
    regform = RegisterForm()
    if regform.validate_on_submit():
        username = regform.username.data
        password = regform.password.data
        name = regform.name.data
        email = regform.email.data
        location = regform.location.data
        biography = regform.biography.data
        photo = regform.photo.data
        filename=secure_filename(photo.filename)
        date_joined = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = User(username, password, name, email, location, biography, filename, date_joined)
        db.session.add(user)
        db.session.commit()
        uid = db.session.query(User.id).all()[-1][0]
        response= {
                    "id": uid,
                    "username": username,
                    "name": name,
                    "photo": filename,
                    "email": email,
                    "location": location,
                    "biography": biography,
                    "date_joined": date_joined
                    }
        return jsonify(response),200
    return jsonify(error=form_errors(regform)),401  

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})
# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")