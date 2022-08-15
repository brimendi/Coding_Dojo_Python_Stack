from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users_model import Users

# READ ALL ROUTE
@app.route('/')
def get_all():
    all_users = Users.get_all()
    return render_template('read_all.html', users = all_users)

# READ ONE USERS INFO
@app.route("/user/<int:id>")
def display_one(id):
    data = {
        "id": id
    }
    user = Users.get_one(data)
    return render_template("read_one.html", user = user)

# CREATE NEW USER
@app.route('/user/new') # first step in creating a user: input new user info page
def new_user_form():
    return render_template('create.html')


@app.route('/user/create', methods=['POST']) # second step in creating a user: info gets saved and redirects to show page with new user info
def create_user():
    id = Users.create_user(request.form)
    return redirect(f'/user/{id}')

# UPDATE A USER INFO 
@app.route('/user/<int:id>/edit') #first step in updating: edit page
def edit_user(id):
    data = {
        "id" : id
    }
    user = Users.get_one(data)
    return render_template("edit.html", user = user)

@app.route('/user/<int:id>/update', methods = ["POST"]) #second step in updating: update and redirect with updates
def update_user(id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": id
    }
    Users.update(data)
    return redirect("/")

# DELETE A USER 
@app.route('/user/<int:id>/delete')
def delete(id):
    data = {
        "id" : id
    }
    Users.delete(data)
    return redirect('/')