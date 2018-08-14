from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity
from api.models.models import DiaryDatabase
from api.validate import Validate
import jwt
import datetime

'''Initialising a flask application'''
app = Flask(__name__)
'''Initialising an empty dictionary'''
CORS(app, resources=r'/api/*')
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'
now = datetime.datetime.now()
db_connect = DiaryDatabase()

def __init__(self):
        DiaryDatabase.__init__(self)
        
@app.route('/api/v1/auth/signup', methods=['POST'])
def register():
    """ registering user """
    data = request.get_json()
    required_fields={"username","password"}
    checkfield = Validate.validate_field(data,required_fields)
    if not checkfield:
        username = data["username"]
        password = data["password"]
        valid = Validate(username, password)
        if username.isalpha() and username.strip() and password.strip() != '' and len(username) >=5 and len(password)>=5 and valid.validate_entry():
            db_connect.cursor.execute("SELECT username FROM tusers where username =%s ", (username,))
            db_connect.conn.commit()
            result = db_connect.cursor.rowcount
            if result == 0:
                db_connect.signup(username,password)
                response = jsonify({"Message":"Created Succesfully"})
                response.status_code = 201
                return response
            else:
                response = jsonify({"Message":"username is invalid, or already taken up! Kindly provide another username"})
                response.status_code = 400
                return response
        else:
            response = jsonify({"Message":"username and password should be provided and *WITH NOT* less than 5 values *EACH*!. Please Avoid such ^{\\s|\\S}*{\\S}+{\\s|\\S}*$ in your username"})
            response.status_code = 400
            return response
    else:
        return jsonify (checkfield),400

@app.route('/api/v1/auth/login', methods=['POST'])
def signin():
    """user login"""
    data = request.get_json()
    required_fields={"username","password"}
    checkfield = Validate.validate_field(data,required_fields)
    if not checkfield:
        username = data["username"]
        password = data["password"]
        valid = Validate(username, password)
        check = db_connect.signin(username, password)
        if valid.validate_entry():
            user = db_connect.signin(username, password)
            return user
        else:
            return jsonify({"Message":"your credentials are wrong! Please check your data field."})
    else:
        return jsonify (checkfield),400

@app.route('/api/v1/entries', methods=['POST'])
@jwt_required
def create_user_entry():
    """create user entries """
    entrydata = request.get_json()
    required_fields={"due_date","name","purpose","type"}
    checkfield = Validate.validate_field(entrydata,required_fields)
    if not checkfield:
        authuser = get_jwt_identity()
        entrydata["user_id"] = authuser["user_id"]
        valid = Validate(entrydata["name"], entrydata["purpose"])
        try:
            date_format = "%Y-%m-%d"
            date_obj = datetime.datetime.strptime(entrydata["due_date"], date_format)
            info = valid.validate_entry()
            if info is True and entrydata["name"].isalpha() and entrydata["type"].isalpha():
                info = db_connect.create_user_entries(entrydata["name"], entrydata["due_date"], entrydata["type"], entrydata["purpose"],entrydata["user_id"])
                return info
            else:
                response = jsonify({"Message": "Please provide a *name* and *purpose* of entry and ensure that all entries are in their valid format!"})
                response.status_code = 400
                return response 
        except ValueError:
            response = jsonify({"Message":"Please Check that your date format suits this format (YYYY-MM-DD)"})
            response.status_code = 400
            return response
    else:
        return jsonify (checkfield),400

@app.route('/api/v1/entries/<entry_id>', methods=['GET'])
@jwt_required
def get_single_entries(entry_id):
    """get all user entries"""
    authuser = get_jwt_identity()
    entryUSER = authuser["user_id"]
    db_connect.cursor.execute("SELECT * FROM tdiaryentries where user_id = %s and id = %s ", (entryUSER, entry_id))
    db_connect.conn.commit()
    result = db_connect.cursor.rowcount
    if result > 0:
        entry = db_connect.get_single_user_entry(entryUSER,entry_id)
        return entry
    else:
        response = jsonify({"Message": "You dont have a specific entry with that *id*!"})
        response.status_code = 400
        return response 

@app.route('/api/v1/entries', methods=['GET'])
@jwt_required
def get_user_entries():
    """get all user entries"""
    authuser = get_jwt_identity()
    entryUSER = authuser["user_id"]
    db_connect.cursor.execute("SELECT * FROM tdiaryentries where user_id = %s", [entryUSER])
    db_connect.conn.commit()
    result = db_connect.cursor.rowcount
    if result > 0:
        entries = db_connect.get_all_user_entries(entryUSER)
        return entries
    else:
        response = jsonify({"Message": "You haven't created any entries yet. Please create first."})
        response.status_code = 200
        return response 

@app.route('/api/v1/entries/<entry_id>', methods=['PUT'])
@jwt_required
def update_user_entry(entry_id):
    entrydata = request.get_json()
    required_fields={"due_date","name","purpose","type"}
    checkfield = Validate.validate_field(entrydata,required_fields)
    if not checkfield:
        authuser = get_jwt_identity()
        entryUSER = authuser["user_id"]
        valid = Validate(entrydata["name"], entrydata["purpose"])
        check = valid.validate_entry()
        try:
            date_format = "%Y-%m-%d"
            date_obj = datetime.datetime.strptime(entrydata["due_date"], date_format)
            if check is True and entrydata["name"].isalpha() and entrydata["type"].isalpha():
                db_connect.cursor.execute("SELECT * FROM tdiaryentries where user_id = %s and id = %s ", (entryUSER, entry_id))
                db_connect.conn.commit()
                result = db_connect.cursor.rowcount
                if result > 0:
                    entry = db_connect.update_user_entryid(entryUSER, entry_id, entrydata["name"], entrydata["due_date"], entrydata["type"], entrydata["purpose"])
                    return entry
                else:
                    response = jsonify({"Message": "You dont have a specific entry with that id!"})
                    response.status_code = 400
                    return response 
            else:
                response = jsonify({"Message": "Please provide a *name* and *purpose* of entry and ensure that all entries are in their valid format!"})
                response.status_code = 400
                return response 
        except ValueError:
            response = jsonify({"Message":"Please Check that your date format suits this format (YYYY-MM-DD)"})
            response.status_code = 400
            return response
    else:
        return jsonify (checkfield),400 


