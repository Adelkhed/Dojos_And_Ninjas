from flask_app import app
from flask_app.config import mysqlconnection
from flask import render_template, redirect,request
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def new_ninja():
    from flask_app.models.dojo import Dojo
    dojos= Dojo.get_all()

    return render_template("new_ninja.html",dojos=dojos)

@app.route('/create/ninja', methods=['POST'])
def save_ninja():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect("/")

@app.route('/ninja/delete/<int:id>')
def delete_ninja(id):
    ninja_to_delete= Ninja.get_ninja({'id':id})
    print("*"*100)
    print(ninja_to_delete)
    
    
    Ninja.delete({'id':id})
    return redirect(f"/dojo/{ninja_to_delete.dojo_id}")

@app.route('/ninja/edit/<int:id>')
def edit_ninjas(id):
    from flask_app.models.dojo import Dojo
    dojos = Dojo.get_all()
    print(dojos)
    ninja_update= Ninja.get_ninja({'id':id})
    print(ninja_update)
    return render_template("edit_ninja.html",dojos=dojos,ninja_update=ninja_update)

@app.route('/update/ninja',methods=['POST'])
def update():
    data= dict(request.form)
      
    print(data)
    Ninja.update_ninja(data)
    return redirect('/')

