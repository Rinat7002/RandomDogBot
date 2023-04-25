import requests

def sendRequest():
    url = "https://random.dog"
    response = requests.get('https://random.dog/woof.json')
    data = response.json()
    return data['url']

