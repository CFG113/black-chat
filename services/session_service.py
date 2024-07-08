# services/session_service.py
from repositories.session_repository import SessionRepository
from repositories.link_repository import LinkRepository

class SessionService:
    @staticmethod
    def create_new_session():
        return SessionRepository.create_session()

    @staticmethod
    def get_session_by_id(session_id):
        return SessionRepository.get_session_by_id(session_id)

    @staticmethod
    def delete_session(session_id):
        LinkRepository.delete_links_by_session_id(session_id)  # Ensure links are deleted first
        return SessionRepository.delete_session(session_id)
