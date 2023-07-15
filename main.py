#Importing necessary libraries
from bson.json_util import dumps
from flask import jsonify, request
from flask import Flask, render_template
from flask_pymongo import PyMongo

#Create new Flask application instance
app = Flask(__name__)
app.config.update(dict(SECRET_KEY='yoursecretkey'))

#Set the MongoDB URI and database name in Flask application configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydb"
mongo = PyMongo(app)

#GET /users 0 Returns a list of all users 
@app.route('/users',methods = ['GET'])
def users():
	users = mongo.db.users.find()
	resp = dumps(users)
	return resp

#GET /users/<id> - Returns the user with the specified ID	
@app.route('/users/<int:id>', methods = ['GET'])
def user(id):
	user = mongo.db.users.find_one({'id': id})
	resp = dumps(user)
	return resp

#POST /users - Creates a new user with the specified data
@app.route('/users',methods = ['POST'])
def create():
	_id = request.form['id']
	_name = request.form['name']
	_email = request.form['email']
	_pwd = request.form['password']
	mongo.db.users.insert_one({
		'id': _id,
		'name':_name,
		'email': _email,
		'password': _pwd})
	return render_template('index.html',message="User created successfully!")

#PUT /users/<id> - Updates the user with the specified ID with the new data
@app.route('/users/<int:id>',methods = ['PUT'])
def update(id):
	_json = request.json
	_name = _json['name']
	_email = _json['email']
	_pwd = _json['password']
	resp = mongo.db.users.find_one_and_update(
		{
			'id': id
		},
		{"$set":
	   {
		   "name": _name,
		   "email": _email,
		   "password": _pwd
	   }}
	)
	resp = "User updated successfully!"
	return resp

#DELETE /users /<id> - Deletes the user with the specified ID with the new data
@app.route('/users/<int:id>',methods = ['DELETE'])
def delete(id):
	mongo.db.users.delete_one({'id': id})
	resp  = 'User deleted successfully!'
	return jsonify(resp)

#Run the Flask application using the Flask run command
if __name__ == "__main__":
    app.run()