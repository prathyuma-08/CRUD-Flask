from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from mongo import MongoCRUD

app = Flask(__name__)
api = Api(app)
mg = MongoCRUD()

class User_single(Resource):
    #Get user by ID
    def get(self,id):
        res = mg.get_id(id)
        return jsonify(res)
    
    #Update a user by ID
    def put(self,id):
        res = mg.update_user(id,
                            request.form['name'],
                            request.form['email'],
                            request.form['password'])
        return jsonify(res)

    #Delete a user by ID
    def delete(self,id):
        res = mg.delete_user(id)
        return jsonify(res)

class User_All(Resource):
    #Get all users
    def get(self):
        res = mg.get_all()
        return jsonify(res)
    
    #Create a new user
    def post(self):
        res = mg.create_user(request.form['id'],
                             request.form['name'],
                             request.form['email'],
                             request.form['password'])
        return jsonify(res)
    

api.add_resource(User_All,'/users')
api.add_resource(User_single,'/users/<int:id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)