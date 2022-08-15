from flask_app import app
from flask import render_template,redirect,request,session,flash

#READ ALL ROUTE 
@app.route('/')
def get_all():
    all_dojos = Dojos.get_all()
    all_ninjas = Ninjas.get_all()
    return render_template('read_all_dojos_and_ninjas.html', dojos = all_dojos, ninjas = all_ninjas)