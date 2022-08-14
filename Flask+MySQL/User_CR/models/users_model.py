from config.mysqlconnection import connectToMySQL
DATABASE = "users_schema"

# USER CLASS CONSTRUCTOR AND ATTRIBUTES
class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # READ ALL METHOD
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        all_users = []
        for row_from_db in results: 
            user_instance = cls(row_from_db)
            all_users.append(user_instance)
        return all_users

    # READ ONE METHOD
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            user_instance = cls(results[0])
            return user_instance
        return results

    # CREATE METHOD
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    # EDIT/UPDATE A USERS INFO
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s " \
            "WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # DELETE USER
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)