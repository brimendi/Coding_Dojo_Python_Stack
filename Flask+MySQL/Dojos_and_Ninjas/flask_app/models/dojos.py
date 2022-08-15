from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojos_and_ninjas"

#DOJOS CLASS CONSTRUCTOR AND ATTRIBUTES 
class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = self.created_at['created_at']
        self.updated_at = self.updated_at['updated_at']

    #READ ALL DOJOS METHOD
    @ classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row_from_db in results:
            dojo_instance = cls(row_from_db)
            all_dojos.append(dojo_instance)
        return all_dojos

    #READ ONE METHOD
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojo WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results: 
            dojo_instance = cls(results[0])
            return dojo_instance
        return results

    #CREATE NEW DOJO METHOD 
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojo (name) VALUES(%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

