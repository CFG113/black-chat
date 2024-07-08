# services/link_service.py
from repositories.link_repository import LinkRepository

class LinkService:
    @staticmethod
    def generate_new_link(session_id):
        return LinkRepository.create_link(session_id)

    @staticmethod
    def mark_link_as_used(link):
        return LinkRepository.update_link(link)
    
    @staticmethod
    def get_session_id_by_link(link_id):
        return LinkRepository.get_session_id_by_link(link_id)

    @staticmethod
    def get_link_by_link(link):
        return LinkRepository.get_link_by_link_id(link)

    @staticmethod
    def delete_link(link):
        return LinkRepository.delete_link(link)
