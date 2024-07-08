# repositories/link_repository.py

from database.init_db import Database
from models.link import Link

db = Database()

class LinkRepository:

    @staticmethod
    def create_link(session_id):
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO links (link_id, session_id, link, is_used) VALUES (gen_random_uuid(), %s, gen_random_uuid()::text, false) RETURNING link;",
            (session_id,)
        )
        link = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        db.close()
        return link
    
    @staticmethod
    def get_session_id_by_link(link_id):
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT session_id FROM links WHERE link = %s;", (link_id,))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result[0] if result else None

    @staticmethod
    def get_link_by_link(link):
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT link_id, session_id, link, is_used FROM links WHERE link = %s;", (link,))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return Link(result[0], result[1], result[2], result[3]) if result else None

    @staticmethod
    def update_link(link):
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE links SET is_used = true WHERE link = %s RETURNING link_id, session_id, link, is_used;", (link,))
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        db.close()
        return Link(result[0], result[1], result[2], result[3]) if result else None

    @staticmethod
    def delete_link(link):
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM links WHERE link = %s;", (link,))
        conn.commit()
        cursor.close()
        db.close()
        return True

    @staticmethod
    def delete_links_by_session_id(session_id):
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM links WHERE session_id = %s;", (session_id,))
        conn.commit()
        cursor.close()
        db.close()
        return True
