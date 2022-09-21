from flask_restx import abort
import requests
import logging

from config import BaseConfig

logger = logging.getLogger(__name__)

MBTA_URL = BaseConfig.MBTA_URL


def _get(url, params=""):
    resp = requests.get(f"{MBTA_URL}/{url}/{params}")
    if resp.status_code != 200:
        abort(400, f"something broke, call support, {resp.reason}")
    return resp.text


# if needed to post to endpoint
def _post(url, payload):
    pass


# if needed to post to endpoint
def _put(url, payload):
    pass
