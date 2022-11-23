from flask import Flask, jsonify, request

class User:
    def signup(self):   #creates class, must extend itself
        user = {    #create user object
            "_id":"",
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        return jsonify(user), 200 #200 = success identifier


