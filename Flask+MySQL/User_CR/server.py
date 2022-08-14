from flask import Flask, render_template, request, redirect
from models.users_model import Users
app = Flask(__name__)                     

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
@app.route('/user/new')
def new_user_form():
    return render_template('create.html')


@app.route('/user/create', methods=['POST'])
def create_user():
    id = Users.create_user(request.form)
    return redirect(f'/user/{id}')

# UPDATE A USER INFO 
@app.route('/user/<int:id>/edit')
def edit_user(id):
    data = {
        "id" : id
    }
    user = Users.get_one(data)
    return render_template("edit.html", user = user)

@app.route('/user/<int:id>/update', methods = ["POST"])
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

if __name__=="__main__":
    app.run(debug=True)