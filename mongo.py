from pymongo import MongoClient
from bson import json_util

class MongoCRUD:
    #Initialize the MongoClient
    def __init__(self):
        self.client = MongoClient('localhost',27017)
        self.db = self.client.mydb
        self.users = self.db.users

    #Get a user using a specified ID
    def get_id(self,userid):
        user = self.users.find_one({'id': userid})
        response = json_util.dumps(user)
        return response
    
    #Get info of all the users
    def get_all(self):
        users = self.users.find()
        response = json_util.dumps(users)
        return response
    
    #Create a single user
    def create_user(self,id,name,email,password):
        _id,_name,_email,_pwd = id,name,email,password
        resp = self.users.insert_one({
		    'id': _id,
		    'name':_name,
		    'email': _email,
		    'password': _pwd})
        print(resp)
        return 'User created successfully'
    
    #Update a single user
    def update_user(self,id,name,email,password):
        _name,_email,_pwd = name,email,password
        resp = self.users.find_one_and_update(
		    {
			    'id': id
		    },
		    {"$set":
	            {
		            "name": _name,
		            "email": _email,
		            "password": _pwd
	            }
            })
        print(resp)
        return 'User updated successfully'
    
    def delete_user(self,id):
        resp = self.users.delete_one({'id': id})
        print(resp)
        return 'User deleted successfully'
