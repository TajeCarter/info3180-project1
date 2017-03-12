from . import db

class Profile(db.Model):
  userid = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  fname = db.Column(db.String(80),nullable=False, index=True)
  lname = db.Column(db.String(80), nullable=False, index=True)
  username = db.Column(db.String(80), index=True, nullable=False, unique=True)
  sex = db.Column(db.String(10), nullable=False, index=True)
  age = db.Column(db.String(25), nullable=False, index=True)
  biography = db.Column(db.String(80), nullable=False)
  image = db.Column(db.String(80), nullable=False) 
  created_on = db.Column(db.DateTime)
  
  def __init__(self, fname, lname, username, sex, age, biography, image, createdon):
    self.fname = fname
    self.lname = lname
    self.username = username
    self.sex = sex
    self.age = age
    self.biography = biography
    self.image = image
    self.created_on = created_on
  

def get_id(self):
  try:
    return unicode(self.userid)
  
  def __repr__(self):
    return "<User %r>" % (self.username)