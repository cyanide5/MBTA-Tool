import json
from functools import lru_cache

from flask_restx import abort

from src.dll.mbta_v1 import _get


@lru_cache(maxsize=128, typed=False)
def get_routes(route=None):
    params = ""
    if route:
        params = f"?filter[route]={route}"
    resp = json.loads(_get("routes", params))
    return [route["id"] for route in resp["data"]]


@lru_cache(maxsize=128, typed=False)
def get_stops(route):
    resp = json.loads(_get("stops", f"?filter[route]={route}"))
    return [route["id"] for route in resp["data"]]
