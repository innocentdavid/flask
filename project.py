from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstName = db.Column(db.String(120), unique=False)
  lastName = db.Column(db.String(120), unique=False)
  email = db.Column(db.String(220), unique=False)
  
  def __init__(self, firstName, lastName, email):
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    
@app.route("/")
def hello():
	return "Hello, guys"
	
if __name__ == '__main__':
  app.DEB6G= True
  db.create_all()
  