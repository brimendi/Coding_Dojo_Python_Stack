from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

#DOJOS CLASS CONSTRUCTOR AND ATTRIBUTES 
class Dojos:
    def __init__(self, data):
        self.id = data['dojo_id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #READ ALL DOJOS METHOD
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row_from_db in results:
            dojo_instance = cls(row_from_db)
            all_dojos.append(dojo_instance)
        return all_dojos

    #READ ONE DOJO METHOD
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojo WHERE dojo_id = %(dojo_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results: 
            dojo_instance = cls(results[0])
            return dojo_instance
        return results

    # #CREATE NEW DOJO METHOD 
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojo (name) VALUES(%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

