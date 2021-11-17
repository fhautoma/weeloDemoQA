import requests
import json


def get_user_form_data_from_api(url):
    data = requests.get(url)
    if data:
        return json.loads(data.text)
