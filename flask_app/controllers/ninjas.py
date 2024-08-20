from flask_app import app
from flask_app.config import mysqlconnection
from flask import render_template, redirect,request
from flask_app.models import ninja,dojo 


@app.route('/ninjas')
def new_ninja():
   
    dojos= dojo.Dojo.get_all()

    return render_template("new_ninja.html",dojos=dojos)

@app.route('/create/ninja', methods=['POST'])
def save_ninja():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    ninja.Ninja.save(data)
    return redirect("/")