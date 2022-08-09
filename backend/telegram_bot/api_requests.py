import requests

url = 'http://127.0.0.1:8000/api/users/'


async def add_user(data):
    response = requests.post(url, data)
    return f"statusCode: {response}, content: {response.content}"



