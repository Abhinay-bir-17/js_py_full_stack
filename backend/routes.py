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

# Create a friend
@app.route("/api/friends",methods=["POST"])
def create_friend():
  try:
    data = request.json

    #validations
    required_fields = ["name","role","description","gender"]
    for field in required_fields:
      if field not in data:
        return jsonify({"error":f"missing required field:{field}"}),400
    
    name = data.get("name")
    role = data.get("role")
    description = data.get("description")
    gender = data.get("gender")

    # Fetch avatar image based on gender
    if gender == "male":
      img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
    elif gender == "female":
      img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
    else:
      img_url = None
    new_friend = Friend(name=name, role=role, description=description, gender= gender, img_url=img_url)
    db.session.add(new_friend) 
    db.session.commit()
    return jsonify({"msg":"Friend created successfully"}),201
    #201 means some resource has been created
  
  except Exception as e:
    db.session.rollback()
    return jsonify({"error":str(e)}), 500

#delete a friend
@app.route("/api/friends/<int:id>",methods=["DELETE"])
def delete_friend(id):
  try:
    friend = Friend.query.get(id)
    if friend is None:
      return jsonify({"error":"Friend not found in db"}),404
    
    db.session.delete(friend)
    db.session.commit()
    return jsonify({"msg":"friend deleted successfully"}), 200
  except Exception as e:
    db.session.rollback()
    return jsonify({"error":str(e)}), 500

#update a friend
@app.route("/api/friends/<int:id>",methods=["PATCH"])
def update_friend(id):
  try:
    friend = Friend.query.get(id)
    if friend is None:
      return jsonify({"error":"Friend not found in db"}),404
    data = request.json
    friend.name = data.get("name", friend.name)#2nd val is default
    friend.role = data.get("role",friend.role)
    friend.description = data.get("description",friend.description)
    friend.gender = data.get("gender",friend.gender)
    
    db.session.commit()
    return jsonify(friend.to_json()), 200
  
  except Exception as e:
    db.session.rollback()
    return jsonify({"error":str(e)}), 500
