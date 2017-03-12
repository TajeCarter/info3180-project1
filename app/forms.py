from flask.ext.wtf import Form
from flask.ext.uploads import *
from wtforms import TextField, RadioField, DateField, FileField
from wtforms.validators import DataRequired, Required, InputRequired
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired

class Profile(Form):
  fname = TextField('fname', validators=[InputRequired()])
  lname = TextField('lname', validators=[InputRequired()])
  username = TextField('username', validators=[InputRequired()])
  sex = RadioField('Sex', choices=[('Male','Male'), ('Female', 'Female')], validators=[InputRequired()])
  biography = TextAreaField('Biography', validators=[InputRequired()])
  age = DateField('age', format='%Y-%m-%d', validators=[DataRequired()])
  image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
  
  
def validate_username(self, field):
  """ Ensures a unique username is chosen """
  # Check if username is already in the database
  if UserProfile.query.filter_by(username=field.data).first():
    # Error message
    self.username.errors.append('Sorry, Username already taken.')