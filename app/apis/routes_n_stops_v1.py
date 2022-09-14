from flask_restx import Namespace, Resource, reqparse
from app.bll.routes_n_stops_v1 import get_routes, get_stops

api = Namespace("v1/", description="Agg Data for Lines and Stops")

stops_parser = reqparse.RequestParser()


@api.route("/all_routes/")
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class RoutesResource(Resource):
    @api.doc(responses={500: ""})
    def get(self):
        return get_routes()


@api.route("/all_stops/")
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class StopsResource(Resource):
    stops_parser.add_argument("route", type=str, location="args")

    @api.expect(stops_parser)
    def get(self):
        args = stops_parser.parse_args()
        return get_stops(args["route"])
