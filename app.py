from flask import Flask
from controllers.youtube_controller import youtube_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(youtube_blueprint, url_prefix="/api/v1")
    return app

app = create_app()



if __name__ == "__main__":
    app = create_app()
    app.run(debug=False, host="0.0.0.0")
