from db_connect import db
from flask import jsonify
from flaskr.models import user


class Auth:
    def signin(data):
        try :
            t_user = db.session.query(user).filter_by(user_id=data.get('user_id')).first()
            
            if t_user is None:
                return jsonify("no user"), 400
            if t_user.user_pw == data.get('user_pw'):
                return jsonify("success"), 200
            else:
                return jsonify("pw fail"), 400
        except Exception as e:
            print(e)
            return jsonify("no user"), 400
