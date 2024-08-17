from flask_app import app
from flask_app.config import mysqlconnection
from flask import render_template, redirect,request
from flask_app.models.dojo import Dojo 

@app.route("/")
def dojos():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def create():
    data={
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route("/dojos")
def det_all_dojo():
    dojos= Dojo.get_all()
    return render_template("index.html", dojos=dojos)

@app.route("/dojos/<int:dojo_id>")
def show_ninjas_of_dojo(dojo_id):
    dojo = Dojo.get_dojo_with_ninjas(dojo_id)
    return render_template("dojo_ninja.html", dojo=dojo)