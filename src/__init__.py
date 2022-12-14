from flask import Flask, Blueprint
import config
import logging
from flask_restx import Api
from flask_restx.apidoc import apidoc

from src.apis.routes_n_stops_v1 import api as routes_n_stops_v1


__version__ = "1.0.0"

URL_PREFIX = config.BaseConfig.URL_PREFIX

app = Flask(__name__)
logger = logging.getLogger(__name__)

apidoc.url_prefix = URL_PREFIX
blueprint = Blueprint("api", __name__, url_prefix=URL_PREFIX)

api = Api(
    blueprint,
    title="MBTA Tool",
    version=__version__,
    description=f"Its a service!",
    catch_all_404s=True,
)

app.register_blueprint(blueprint)

api.add_namespace(routes_n_stops_v1)
