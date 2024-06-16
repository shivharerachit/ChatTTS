from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from core_apis.view import api

def create_app(api):
    app = Flask(__name__)
    CORS(app)


    from core_apis.view import chatgpt
    app.register_blueprint(chatgpt)

    api.init_app(app)

    from core_apis.view import chatgpts
    api.add_namespace(chatgpts)

    return app





app = create_app(api)


if __name__=='__main__':
    app.run("0.0.0.0", port=8080, debug=True, use_reloader=True)