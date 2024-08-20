from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route("/")
def home():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)

@app.route("/create/dojo", methods=['POST'])
def create():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route('/dojo/<int:id>')
def show_ninjas_of_dojo(id):
    dojo = Dojo.get_dojo_with_ninjas({'id': id})
    return render_template("dojo_ninja.html", dojo=dojo)
