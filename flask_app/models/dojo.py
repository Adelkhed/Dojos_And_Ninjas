from flask_app.config.mysqlconnection import connectToMySQL,DB
from flask_app.models.ninja import Ninja
class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
    @classmethod
    def save(cls,data):
        query="INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos;"
        results = connectToMySQL(DB).query_db(query)
        dojos=[]
        for result in results:
            dojo= cls(result)
            dojos.append(dojo)
        return dojos
     
    @classmethod
    def get_dojo_with_ninjas(cls, dojo_id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
        data = {'dojo_id': dojo_id}
        results = connectToMySQL(DB).query_db(query, data)

        dojo = cls(results[0])
        dojo.ninjas = []
        for result in results:
            ninja_data = {
                'id': result['ninjas.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'age': result['age'],
                'created_at': result['ninjas.created_at'],
                'updated_at': result['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo