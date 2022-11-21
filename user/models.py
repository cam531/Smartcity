from flask import Flask, jsonify

class User:
    def signup(self):   #creates class, must extend itself
        user = {    #create user object
            "_id":"",
            "name":"",
            "email":"",
            "password":""
        }
        return jsonify(user), 200 #200 = success identifier
        

