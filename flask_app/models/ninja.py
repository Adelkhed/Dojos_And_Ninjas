from flask_app.config.mysqlconnection import connectToMySQL,DB

class Ninja:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.dojo=None
    @classmethod
    def save(cls,data):
        query="INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def get_all(cls):
        from flask_app.models.dojo import Dojo  # Importation à l'intérieur de la méthode pour éviter la boucle
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
            ninja.dojo = Dojo(dojo_data)
            ninjas.append(ninja)
        return ninjas