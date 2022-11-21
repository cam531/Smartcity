#contains all routes related to the user. 
# user/login, user/register, etc.

from flask import Flask
from app import app     #from app.py imports the flask app
from user.models import User    #imports user object from the models.py file

@app.route('/user/signup', methods = ['GET'])
def signup():
    return User().signup() #creates a new user class instance
