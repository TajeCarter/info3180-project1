from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "S3cR3+K3y"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:password@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models