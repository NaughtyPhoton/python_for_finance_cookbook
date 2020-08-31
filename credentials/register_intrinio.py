import json
import os

_INTRINIO_JSON = f'{os.path.expanduser("~")}/.credentials/intrinio.json'
print(_INTRINIO_JSON)
with open(_INTRINIO_JSON) as f:
    asJson = json.load(f)
    INTRINIO_SANDBOX = asJson['api_sandbox']
    INTRINIO_PRODUCTION = asJson['api_production']
