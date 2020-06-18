from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	header="Welcome to Flask"
	return render_template("index.html", headline=header)

@app.route("/bye")
def bye():
	header="Goodbye"
	return render_template("index.html", headline=header)

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	return (f"<h1>{name} is not available!</h1>")
