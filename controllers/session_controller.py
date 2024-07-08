# controllers/session_controller.py
from flask import Blueprint, jsonify, request
from services.session_service import SessionService
from utils.error_handler import handle_errors, bad_request, not_found, internal_server_error

session_bp = Blueprint('session_bp', __name__, url_prefix='/sessions')

@session_bp.route('/')
@handle_errors
def index():
    return "Welcome to BlackChat!", 200  # 200 OK

@session_bp.route('/create', methods=['POST'])
@handle_errors
def create_session():
    session = SessionService.create_new_session()
    if not session:
        return internal_server_error("Failed to create session")
    return jsonify(session_id=session.session_id), 201  # 201 Created

@session_bp.route('/<session_id>', methods=['GET'])
@handle_errors
def get_session(session_id):
    session = SessionService.get_session_by_id(session_id)
    if not session:
        return not_found("Session not found")
    return jsonify(session_id=session.session_id), 200  # 200 OK

@session_bp.route('/end-session', methods=['DELETE'])
@handle_errors
def end_session():
    data = request.json
    session_id = data.get('session_id')
    if not session_id:
        return bad_request("session_id is required")
    if not SessionService.get_session_by_id(session_id):
        return not_found("Session not found")
    SessionService.delete_session(session_id)
    return '', 204  # 204 No Content
