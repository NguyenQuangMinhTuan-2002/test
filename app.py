from flask import Flask
from config import Config
from flask_cors import CORS
from extensions import db  # import từ file mới
from controllers.user_controller import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    app.register_blueprint(user_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)