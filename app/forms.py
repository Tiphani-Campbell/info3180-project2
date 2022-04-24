# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, EmailField, PasswordField, SelectField, DecimalField
from wtforms.validators import DataRequired, Email, InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    name = StringField("Fullname", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    location = StringField("Location", validators=[DataRequired()])
    biography = TextAreaField("Biography", validators=[DataRequired()])
    photo = FileField('Upload Photo', validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'],'Image files only')])

class CarForm(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])
    colour = StringField("Colour", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    type = SelectField('Car Type', validators=[DataRequired()], choices=[('SUV', 'SUV'), ('Truck', 'Truck'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback')])
    transmission = SelectField('Transmission', choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')])
    description = TextAreaField("Description", validators=[DataRequired()])
    photo = FileField('Upload Photo', validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'],'Image files only')])

class SearchForm(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])