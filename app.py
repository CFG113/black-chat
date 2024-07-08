from flask import Flask
from flask_cors import CORS

from controllers.link_controller import link_bp
from controllers.session_controller import session_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(session_bp)
app.register_blueprint(link_bp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)