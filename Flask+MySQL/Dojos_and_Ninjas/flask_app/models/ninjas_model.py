from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# NINJAS CLASS CONSTRUCTOR AND ATTRIBUTES
class Ninjas:
    def __init__(self, data):
        self.id = data['ninjas_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

# GET ALL NINJAS INFO 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        for row_from_db in results:
            ninjas_instance = cls(row_from_db)
            all_ninjas.append(ninjas_instance)
        return all_ninjas
    
    # CREATE A NEW NINJA ACTION 
    @classmethod 
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    # GET ALL NINJAS UNDER ONE SINGLE DOJO
    @classmethod
    def get_all_by_dojo(cls, dojo_id):
        query = f"SELECT * FROM ninjas WHERE dojo_id = {dojo_id}"
        results = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        if results:
            for row_from_db in results:
                ninjas_instance = cls(row_from_db)
                all_ninjas.append(ninjas_instance)
        return all_ninjas
