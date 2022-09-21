from flask import Flask
from flask_caching import Cache
from flask_restx import Namespace, Resource, reqparse

import config
from src.bll.routes_n_stops_v1 import get_routes, get_stops

api = Namespace("v1/", description="Agg Data for Lines and Stops")

stops_parser = reqparse.RequestParser()

app = Flask(__name__)
app.config.from_object('config.RedisConfig')
cache = Cache(app)


@api.route("/all_routes/")
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class RoutesResource(Resource):
    @api.doc(responses={500: ""})
    @cache.cached(timeout=30, query_string=True)
    def get(self):
        return get_routes()


@api.route("/all_stops/")
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class StopsResource(Resource):
    stops_parser.add_argument("route", type=str, location="args")

    @api.expect(stops_parser)
    @cache.cached(timeout=30, query_string=True)
    def get(self):
        args = stops_parser.parse_args()
        return get_stops(args["route"])
