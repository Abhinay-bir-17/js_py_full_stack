from app import app,db
from flask import request, jsonify
from models import Friend

# Get all friends
@app.route("/api/friends",methods=["GET"])
def get_friends():
  '''below  we didnt write select * from friends '''
  ''' friends will be in python objects representation '''
  friends = Friend.query.all() 
  result = [friend.to_json() for friend in friends] # list comprehension
  # result will look like :,[{...}, {...} ....]
  return jsonify(result) #status code is 200 by default

