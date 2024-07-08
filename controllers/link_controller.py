# controllers/link_controller.py
from flask import Blueprint, jsonify, request
from services.link_service import LinkService
from utils.error_handler import handle_errors, bad_request, not_found, gone, internal_server_error

link_bp = Blueprint('link_bp', __name__, url_prefix='/links')

@link_bp.route('/generate', methods=['POST'])
@handle_errors
def generate_link():
    data = request.json
    session_id = data.get('session_id')
    if not session_id:
        return bad_request("session_id is required")
    link = LinkService.generate_new_link(session_id)
    if not link:
        return internal_server_error("Failed to generate link")
    return jsonify(link=link), 201

@link_bp.route('/session/<link_id>', methods=['GET'])
@handle_errors
def get_session_id_by_link(link_id):
    session_id = LinkService.get_session_id_by_link(link_id)
    if not session_id:
        return not_found("Session ID not found for the given link")
    return jsonify(session_id=session_id), 200  # 200 OK

@link_bp.route('/join/<link>', methods=['PUT'])
@handle_errors
def join_session(link):
    link_obj = LinkService.get_link_by_link_id(link)
    if not link_obj:
        return not_found("Link not found")
    if link_obj.is_used:
        return gone("Link already used")
    LinkService.mark_link_as_used(link)
    return jsonify(success=True), 200  # 200 OK

@link_bp.route('/<link>', methods=['DELETE'])
@handle_errors
def delete_link(link):
    link_obj = LinkService.get_link_by_link(link)
    if not link_obj:
        return not_found("Link not found")
    LinkService.delete_link(link)
    return '', 204  # 204 No Content
