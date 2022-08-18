from crypt import methods
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import Users
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/login_and_registration')
def login_and_register_form():
    if "user_id" in session:
        return redirect('/dashboard')
    return render_template("login_and_registration.html")

@app.route('/dashboard')
def dashboard():
    if not "user_id" in session:
        return redirect('/login_and_registration')
    return render_template("dashboard.html")

@app.route('/users/register', methods=['POST'])
def register():
    print(request.form)
    if not Users.validate(request.form):
        return redirect('/login_and_registration')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_pw
    }
    session['user_id'] = Users.create(data)
    return redirect('/dashboard')

@app.route('/users/logout')
def logout():
    if "user_id" in session:
        del session['user_id']
    return redirect('/login_and_registration')

@app.route('/users/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_from_db = Users.get_by_email(data)
    if not user_from_db:
        flash("Invalid credentials", "log")
        return redirect('/login_and_registration')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        flash("Invalid credentials", "log")
        return redirect('/login_and_registration')

    session['user_id'] = user_from_db.id
    return redirect('/dashboard')