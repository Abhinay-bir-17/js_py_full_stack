# https://github.com/burakorkmez/react-python-tutorial/tree/master 
# https://www.youtube.com/watch?v=tWHXaSC2T_s    ( 30:10 min )

# do flask run to run app.py
# app.py is the entry point to our app
# used 'python app.py' to run in venv
''' then to view http://127.0.0.1:5000/api/friends
this gives error, so stop the server nd do this
set FLASK_APP=app.py(no spaces around =)
set FLASK_ENV = development
nd then do ' flask run' ,
next flask run --reload
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  
app = Flask(__name__)
CORS(app)

# friends is our db name
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False   

db = SQLAlchemy(app)

# as routes aint returin anything so we dont need to say from
# import routes 
import routes 
#  do the below to create a db, then do flask run
with app.app_context():
  db.create_all() #creates columns of db

# below means when we run this file then only run app, it prevents
# app.run to execute if it has been imported by other files
if __name__=="__main__":
    app.run(debug=True)
