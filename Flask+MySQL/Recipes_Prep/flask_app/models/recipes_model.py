from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
import re 

class Recipes:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, instruction, under_30_min, user_id) VALUES(%(name)s, %(description)s, %(instruction)s, %(under_30_min)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod 
    def edit_recipes(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, under_30_min = %(under_30_min)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN user ON recipes.user_id=user.id"
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        if results: 
            for row in results:
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id': row['user.id'],
                    'created_at': row['user.created_at'],
                    'updated_at': row['user.updated_at'],
                }
                this_user = user_model.Users(user_data)
                this_recipe.planner = this_user
                all_recipes.append(this_recipe)
        return all_recipes

    @classmethod 
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN user on user.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        this_recipe = cls(row)
        user_data = {
            **row,
            'id': row['user.id'],
            'created_at': row['user.created_at'],
            'updated_at': row['user.updated_at']
        }
        planner = user_model.Users(user_data)
        this_recipe.plammer = planner
        return this_recipe

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(form_info):
        is_valid = True
        if len(form_info['name']) < 1:
            flash("name is required")
            is_valid = False
        if len(form_info['description']) < 1:
            flash("description is required")
            is_valid = False
        if len(form_info['instruction']) < 1:
            flash("instructions are required")
            is_valid = False
        if len(form_info['date']) < 1:
            flash("date is required")
            is_valid = False
        if "under_30_min" not in form_info:
            flash("under 30 minutes? required")
            is_valid = False
        return is_valid