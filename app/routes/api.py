from flask import Blueprint, request, jsonify
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

    #create a new user
    try:
        newUser = User(
            username=data['username'],
            email= data['email'],
            password= data['password']
        )

    #save new user to db

        db.add(newUser)
        db.commit()

    except:
        return jsonify(message='Signup failed'), 500
    return jsonify(id='newUser.id')