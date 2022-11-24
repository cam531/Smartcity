from flask import Flask, jsonify, request
#from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class User:
    def signup(self):   #creates class, must extend itself
        print(request.form)

        #create user object
        user = { 
            #create user id   
            "_id": uuid.uuid4().hex, 
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        #encrypt password
        #user['password'] = pbkdf2_sha256.encrypt(user['password'])

        #passing user object to database
        db.users.insert_one(user)   

        return jsonify(user), 200 


