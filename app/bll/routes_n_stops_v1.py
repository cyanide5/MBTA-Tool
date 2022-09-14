import json
from app.dll.mbta_v1 import _get


def get_routes(route=None):
    params = ''
    if route:
        params = f'?filter[route]={route}'

    resp = json.loads(_get('routes', params))
    return [route['id'] for route in resp['data']]


def get_stops(route):
    resp = json.loads(_get('stops', f'?filter[route]={route}'))
    return [route['id'] for route in resp['data']]