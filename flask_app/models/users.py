from flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data): 
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
    
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO user (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s,%(email)s)"
        result = connectToMySQL('crud').query_db(query, formulario)
        return result

    @classmethod
    def muestra_usuarios(cls):
        query ="SELECT * FROM crud.user "
        results = connectToMySQL('crud').query_db(query)
        users = []
        for u in results:          
            instancia_usuario = cls(u)
            users.append(instancia_usuario)
        return users

    @classmethod
    def borrar(cls, formulario):
        query = "DELETE FROM crud.user WHERE id = %(id)s"
        result = connectToMySQL('crud').query_db(query, formulario)
        return result
    

    @classmethod
    def muestra_usuario(cls,formulario):
        query ="SELECT * FROM crud.user WHERE id = %(id)s"
        results = connectToMySQL('crud').query_db(query,formulario)
        
        return results
        

    @classmethod
    def update(cls,formulario):
        query ="UPDATE crud.user SET first_name = %(first_name)s , last_name = %(last_name)s, email =  %(email)s WHERE id = %(id)s"
        results = connectToMySQL('crud').query_db(query,formulario)
        
        return results

