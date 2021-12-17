import requests
import json


def get_json(request_url):
    if request_url is None:
        return ''
    if 'https://api.hypixel.net/' not in request_url:
        return ''
    try:
        r = json.loads(requests.get(request_url))
        return r
    except:
        return ''
