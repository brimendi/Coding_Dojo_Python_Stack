from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojos_model import Dojos
from flask_app.models.ninjas_model import Ninjas

#READ ALL ROUTE 
@app.route('/dojos')
def get_all_dojos_and_ninjas():
    all_dojos = Dojos.get_all()
    all_ninjas = Ninjas.get_all()
    return render_template("read_all_dojos_and_ninjas.html", all_dojos = all_dojos, all_ninjas = all_ninjas)

#NEW DOJO FORM
@app.route('/dojos/new')
def new_dojo_form():
    all_dojos = Dojos.get_all()
    return render_template("show_one_dojo.html", all_dojos = all_dojos)

#CREATE NEW DOJO ACTION
@app.route('/dojos/create', methods=["POST"])
def dojo_create():
    dojo_id = Dojos.create_dojo(request.form)
    return redirect(f'/dojos/{dojo_id}')

#SHOW ONE DOJO PAGE
@app.route('/dojos/<int:dojo_id>')
def display_one_dojo(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    dojos = Dojos.get_one_dojo(data)
    ninjas = Ninjas.get_all_by_dojo(dojo_id)
    return render_template("show_one_dojo.html", dojos = dojos, ninjas = ninjas)
