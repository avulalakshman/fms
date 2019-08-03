from flask import Flask, json, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
dept = [
    {
        "name":"CSE",
        "faculties":[
            {"name":"Lakshman","qualification":"M.Tech","exp":10}
        ]
    }
]

@app.route('/dept',methods=["POST"])
def add_dept():
    req_data = request.get_json()
    new_dept = {
        "name" : req_data["name"],
        "faculties": req_data["faculties"]
    }
    dept.append(new_dept)
    return json.jsonify(new_dept)

@app.route('/dept/<string:name>')
def get_dept(name):

    for d in dept:
        if d["name"] == name:
            return json.jsonify(d)
    return json.jsonify({"message":f"Department is not found with name {name}"})

    

@app.route('/dept')
def get_depts():
    return json.jsonify(dept)

@app.route('/dept/<string:name>/faculty',methods=["POST"])
def add_faculty(name):
    request_data = request.get_json()
    for d in dept:
        if d["name"] == name:
            faculty={
                "name" : request_data["name"],
                "qualfication":request_data["qualification"]
            }
            d["faculties"].append(faculty)
            return json.jsonify(faculty)
    return json.jsonify({"message":f"Department is not found with name {name}"})

@app.route("/dept/<string:name>/faculties")
def get_faculties(name):
    for d in dept:
        if d["name"] == name:
            return json.jsonify(d["faculties"])
    return json.jsonify({"message":f"Department is not found with name {name}"})



if __name__ == "__main__":
    app.run(port = 5000)