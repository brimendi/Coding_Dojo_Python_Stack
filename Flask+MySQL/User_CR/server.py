from flask import Flask, render_template, request, redirect
from users_model import Users
app = Flask(__name__)                     

# READ ALL ROUTE
@app.route('/')
def get_all():
    all_users = Users.get_all()
    return render_template('read_all.html', users = all_users)

# INPUT NEW USER INFO
@app.route('/user/new')
def new_user_form():
    return render_template('create.html')

# CREATE NEW USER
@app.route('/user/create', methods=['POST'])
def create_user():
    Users.create_user(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)