
def fetch_api_data(url):
    import requests
    response = requests.get(url)
    data = response.json()
    return data
url = 'https://api.thecatapi.com/v1/breeds'
data = fetch_api_data(url)
print(data)