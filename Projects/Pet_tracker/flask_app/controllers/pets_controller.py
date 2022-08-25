from flask_app import app
import re
from flask import render_template,redirect,request,session,flash
from flask_app.models.pets_model import Pets
from flask_app.models.user_model import Users
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/mypets/add')
def add_pet():
    if not "user_id" in session:
        return redirect('/login_and_registration')
    user = Users.get_by_id({'id': session['user_id']})
    data = {
        'id': id
    }
    pet = Pets.create(data)
    return render_template("add_pet.html", user = user, pet = pet)

@app.route('/mypets/create',methods=['POST'])
def create_pet():
    if not "user_id" in session:
        return redirect('/login_and_registration')
    if not Pets.validator(request.form):
        return redirect('/mypets/add')
    data = {
        **request.form, 
        'user_id': session['user_id']
    }
    # print(request.form)
    Pets.create(data)
    return redirect('/mypets/home')

@app.route('/mypets/view_one/<int:id>')
def view_one(id):
    if not "user_id" in session:
        return redirect('/login_and_registration')
    data = {
        'id': id
    }
    pet = Pets.get_by_id(data)
    data = {
        'id': pet.users_id
    }
    user = Users.get_by_id(data)
    return render_template('view_one_pet.html', pet = pet, user = user)

@app.route('/mypets/edit/<int:id>')
def edit_pet(id):
    if not "user_id" in session:
        return redirect ('/login_and_registration')
    pet = Pets.get_by_id({'id': id})
    return render_template("edit_pet.html", pet = pet)

@app.route('/mypets/update/<int:id>', methods=['POST'])
def update_pet(id):
    if not "user_id" in session:
        return redirect('/login_and_registration')
    if not Pets.validator(request.form):
        return redirect(f'/mypets/edit/{id}')
    data = {
        **request.form,
        'id':id
    }
    Pets.edit_pet(data)
    return redirect(f'/mypets/view_one/{id}')

@app.route('/mypets/budget')
def budget():
    if not "user_id" in session:
        return redirect('/login_and_registration')
    return redirect('/mypets/budget')

# @app.route('/mypets/add')
# def upload_image():
#     if "file" not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#     if file.fiilename == '':
#         flash('No image selected for uploading')
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         flash("Image succesfully uploaded")
#         return render_template("add_pet.html", filename=filename)
#     else:
#         flash('Allowed image types are - png, jpg, jpeg, gif')
#         return redirect(request.url)