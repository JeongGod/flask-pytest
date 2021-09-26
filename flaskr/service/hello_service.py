from flask import jsonify


class Test:
    def get_hello():
        return jsonify("Hello World"), 200
