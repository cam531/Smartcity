from flask import Flask, render_template
import pymongo
from user.models import User    #imports user object from the models.py file

app = Flask(__name__) #app is an instance of Flask

#Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system


#Routes

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route('/user/signup', methods = ['POST']) 
def signup():
    return User().signup() #creates a new user class instance


############################
if __name__ == "__main__":
    app.run(port = 5000, debug = True)