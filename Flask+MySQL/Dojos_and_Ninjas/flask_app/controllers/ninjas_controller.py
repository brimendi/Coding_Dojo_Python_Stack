from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojos_model import Dojos
from flask_app.models.ninjas_model import Ninjas

# NEW NINJA FORM
@app.route('/ninja/new')
def new_ninja_form():
    all_dojos = Dojos.get_all()
    return render_template("create_new_ninjas.html", dojos=all_dojos)

# CREATE NEW NINJA ACTION- REDIRECT TO -SHOW ONE DOJO- PAGE W/ UPDATED NINJA
@app.route('/ninja/create', methods=["POST"])
def ninja_create():
    Ninjas.create(request.form)
    Dojos.get_one_dojo(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")
