# app.py
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, send

from controllers.link_controller import link_bp
from controllers.session_controller import session_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(session_bp)
app.register_blueprint(link_bp)

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# Define WebSocket event for handling messages
@socketio.on('message')
def handle_message(msg):
    print(f'Message: {msg}')
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)
