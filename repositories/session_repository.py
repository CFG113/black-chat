# repositories/session_repository.py

from database.init_db import Database
from models.session import Session

db = Database()

class SessionRepository:

    @staticmethod
    def create_session():
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sessions (session_id) VALUES (gen_random_uuid()) RETURNING session_id;")
        session_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        db.close()
        return Session(session_id) if session_id else None

    @staticmethod
    def get_session_by_id(session_id):
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT session_id FROM sessions WHERE session_id = %s;", (session_id,))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return Session(result[0]) if result else None

    @staticmethod
    def delete_session(session_id):
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sessions WHERE session_id = %s;", (session_id,))
        conn.commit()
        cursor.close()
        db.close()
        return True
