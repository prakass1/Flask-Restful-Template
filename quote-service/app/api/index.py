from app import __version__ as info
from flask import jsonify
from flask_restx import Resource, Api, Namespace

index_api = Namespace("index", description="Index API")


@index_api.route("")
class BaseResource(Resource):
    def get(self):
        return jsonify(
            {
                "title": info.__title__,
                "version": info.__version__,
                "description": info.__description__,
            }
        )