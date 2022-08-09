import json

import requests


def keitario_get_statistic(url, date_from, date_to, token):
    data = {
        "range": {
            "from": f"{date_from}",
            "to": f"{date_to}",
            "timezone": "Europe/Kiev"
        }
    }
    try:
        response = requests.post(url, json=data, headers={'Api-Key': f'{token}'})
    except requests.exceptions.MissingSchema:
        return {'statusCode': 400}
    return {'statusCode': response.status_code, 'url': str(response.request.url)[-10:], 'content': json.loads(response.text)}
