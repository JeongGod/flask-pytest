from flask import Blueprint, request
from flask.json import jsonify
from flaskr.models.user import *

bp2 = Blueprint('bp2', __name__, url_prefix='/api/signin')

@bp2.route('', methods=['POST'])
def test():
    info = request.json
    try :
        t_user = db.session.query(user).filter_by(user_id=info.get('user_id')).first()
        
        if t_user is None:
            return jsonify("no user"), 400
        if t_user.user_pw == info.get('user_pw'):
            return jsonify("success"), 200
        else:
            return jsonify("pw fail"), 400
    except Exception as e:
        print(e)
        return jsonify("no user"), 400

