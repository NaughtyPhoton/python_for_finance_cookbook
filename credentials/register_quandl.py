import json
import os

_QUANDL_JSON = f'{os.path.expanduser("~")}/.credentials/quandl.json'
with open(_QUANDL_JSON) as f:
    QUANDL_KEY = json.load(f)['api_key']
