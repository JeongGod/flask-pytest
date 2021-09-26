from flask import Blueprint, request
from flaskr.service.hello_service import Test

bp = Blueprint('bp', __name__, url_prefix='/api/hello')

@bp.route('', methods=['GET'])
def test():
    return Test.get_hello()

