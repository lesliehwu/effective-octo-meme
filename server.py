from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninjas")
def ninjas():
    return render_template("ninjas.html")

@app.route("/dojos/new",methods=['POST','GET'])
def new_dojos():
    return render_template("new_dojos.html")
    fave_dog = request.form["fave_dog"]
    fave_tv = request.form["fave_tv"]
    return redirect(url_for("/"))

app.run(debug = True)
