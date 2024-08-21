from flask_app.config.mysqlconnection import connectToMySQL,DB
from flask_app.models import dojo 
class Ninja:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.dojo_id=None
    @classmethod
    def save(cls,data):
        query="INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def get_all(cls):
         
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id;"
        results = connectToMySQL(DB).query_db(query)
        ninjas = []
        for result in results:
            ninja = cls(result)
            dojo_data = {
                'id': result['dojos.id'],
                'name': result['name'],
                'created_at': result['dojos.created_at'],    
                'updated_at': result['dojos.updated_at']
            }
            ninja.dojo = dojo.Dojo(dojo_data)
            ninjas.append(ninja)
        return ninjas
    
    @classmethod
    def get_ninja(cls,data):
        query = " SELECT * FROM ninjas WHERE id= %(id)s"
        result = connectToMySQL(DB).query_db(query,data)
        ninja=cls(result[0])
        ninja.dojo_id = result[0]['dojo_id']
        print("ninja")
        print(ninja.dojo_id)
        return ninja
    
        
        

   
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM ninjas Where id =%(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        return result
    @classmethod
    def update_ninja(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s WHERE id=%(id)s;"
        print(query)
        return connectToMySQL(DB).query_db(query,data)