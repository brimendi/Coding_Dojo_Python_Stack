from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re 
ALPHANUMERIC = re.compile(r"[a-zA-Z0-9]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")


#LOGIN/REGISTRATION CLASS CONSTRUCTOR AND ATTRIBUTES  
class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod 
    def get_by_email(cls, data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['first_name']) < 2: 
            flash("First name must be at least 2 characters", "reg")
            is_valid = False
        elif not ALPHANUMERIC.match(user_data['first_name']):
            flash("First name cannot contain special chars")
            is_valid = False
        if len(user_data['last_name']) < 2:
            flash("Last name must be at least 2 characters", "reg")
            is_valid = False
        elif not ALPHANUMERIC.match(user_data['last_name']):
            flash("Last name cannot contain special chars")
            is_valid = False
        if len(user_data['email']) < 1:
            flash("Please provide an email", "reg")
            is_valid = False
        elif not EMAIL_REGEX.match(user_data['email']):
            flash("Invalid email", "reg")
            is_valid = False
        else:
            data = {
                'email': user_data['email']
            }
            potential_user = Users.get_by_email(data)
            if potential_user:
                is_valid = False
                flash("An account already exists with this email")

        if len(user_data['password']) < 8:
            flash("Password must be at least 8 characters", "reg")
            is_valid = False
        elif not user_data['password'] == user_data['confirm_password']:
            flash("Passwords don't match")
            is_valid = False

        return is_valid

        