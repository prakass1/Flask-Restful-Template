from flask import Flask
from flask_restx import Api
from app.config import app_config
from flask_cors import CORS
def create_app(config_env):
    app = Flask(__name__)
    app.logger.info(f"Config name -- {config_env}")

    authorizations = {
        "api-key": {"type": "apiKey", "in": "header", "name": "Authorization"}
    }
    app.config.from_object(app_config[config_env])#
    api = Api(
        app,
        title="Quotes api",
        version="1.0.0",
        doc="/api/v1/docs",
        authorizations=authorizations,
    )
    CORS(app)
    register_routes(api, app)
    return app

def register_routes(api, app, root="api/v1"):
    from app.api.index import index_api
    from app.api.quotes import quotes_api
    # Add any routes here..
    api.add_namespace(index_api, path=f"/{root}/index")
    api.add_namespace(quotes_api, path=f"/{root}/quotes")
