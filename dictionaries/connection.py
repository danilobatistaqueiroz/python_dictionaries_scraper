import requests

def get_data(word, path):
    data = requests.get(f'{path}/{word}').json()
    return data