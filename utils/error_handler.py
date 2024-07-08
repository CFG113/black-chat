from flask import jsonify
from functools import wraps

def handle_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            return bad_request(str(e))
        except KeyError as e:
            return not_found(str(e))
        except Exception as e:
            return internal_server_error(str(e))
    return decorated_function

def bad_request(message):
    response = jsonify({'error': message})
    response.status_code = 400
    return response

def not_found(message):
    response = jsonify({'error': message})
    response.status_code = 404
    return response

def gone(message):
    response = jsonify({'error': message})
    response.status_code = 410
    return response

def internal_server_error(message):
    response = jsonify({'error': message})
    response.status_code = 500
    return response
