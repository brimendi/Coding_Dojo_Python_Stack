from crypt import methods
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import Users
from flask_app.models.recipes_model import Recipes
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# NEW RECIPES FORM 
@app.route('/recipes/new')
def new_recipe_form():
    if not "user_id" in session:
        return redirect('/login_and_registration')
    user = Users.get_by_id({'id': session['user_id']})
    return render_template("new_recipe.html", user = user)

# NEW RECIPE ACTION 
@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if not "user_id" in session:
        return redirect('/login_and_registration')
    if not Recipes.validator(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form, 
        'user_id': session['user_id']
    }
    Recipes.create(data)
    return redirect('/dashboard')

# EDIT RECIPE FORM 
@app.route('/recipes/<int:id>/edit')
def edit_recipes_form(id):
    if not "user_id" in session:
        return redirect ('/login_and_registration')
    recipe = Recipes.get_by_id({'id': id})
    return render_template("edit_recipe.html", recipe = recipe)
    
# EDITED RECIPE ACTION 
@app.route('/recipes/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if not "user_id" in session:
        return redirect('/login_and_registration')
    if not Recipes.validator(request.form):
        return redirect(f'/recipes/{id}/edit')
    data = {
        **request.form,
        'id':id
    }
    Recipes.edit_recipes(data)
    return redirect('/dashboard')

# DELETE RECIPE ACTION 
@app.route('/recipes/<int:id>/delete')
def delete_recipes(id):
    if not "user_id" in session:
        return redirect('/login_and_registration')
    data = {
        'id':id
    }
    getting_deleted = Recipes.get_by_id(data)
    if not session['user_id'] == getting_deleted.user_id:
        flash("this recipe is not yours to delete")
        return redirect('/login_and_registration')
    Recipes.delete(data)
    return redirect('/dashboard')

# VIEW ONE RECIPE 
@app.route('/recipes/<int:id>')
def show_one_recipe(id):
    if not "user_id" in session:
        return redirect('/login_and_registration')
    data = {
        'id': id
    }
    user = Users.get_by_id(data)
    recipe = Recipes.get_by_id(data)
    return render_template('recipe_one.html', recipe = recipe, user = user)