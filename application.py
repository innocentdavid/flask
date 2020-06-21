from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	header="Welcome to Flask"
	return render_template("index.html", headline=header)

@app.route("/css")
def css():
	return render_template("css.html")

@app.route("/js")
def js():
	return render_template("js.html")

@app.route("/html")
def html():
	return render_template("html.html")

@app.route("/py")
def py():
	return render_template("py.html")

@app.route("/dj")
def dj():
	return render_template("dj.html")	

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	return (f"<h1>{name} is not available!</h1>")
	
if __name__ == '__main__':
  app.DEB6G= True
  app.run(host ='127.0.0.1', port=5000)