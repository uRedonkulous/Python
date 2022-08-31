from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name['first_name']
        self.last_name['last_name']
        self.email['email']
        self.created_at['created_at']
        self.updated_at['updated_at']

@classmethod
def get_all(cls):
    query = "SELECT * FROM users;"
    results = connectToMySQL('users_schema').query_db(query)
    users = []
    for u in results:
        users.append (cls(u))
    return users

@classmethod
def save(cls, data):
    query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
    result = connectToMySQL('users_schema').query_db(query, data)
    return result