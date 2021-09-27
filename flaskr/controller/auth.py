from flask import Blueprint, request
from flaskr.service.auth_service import Auth

bp2 = Blueprint('bp2', __name__, url_prefix='/api/signin')

@bp2.route('', methods=['POST'])
def test():
    info = request.json
    return Auth.signin(info)

