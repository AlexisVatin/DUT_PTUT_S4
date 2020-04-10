import requests


def translate(apiurl, apikey, word):
    payload = {'key': apikey, 'text': word, 'lang': 'fr-en'}
    raw_data = requests.get(apiurl, params=payload)
    json_data = raw_data.json()
    return json_data['text']
