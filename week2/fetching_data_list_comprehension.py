import requests
from pprint import pprint

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats = response.json()

cat_weights = [(float(cat['weight']['metric'].split()[0]) + float(cat['weight']['metric'].split()[2])) / 2 for cat in cats ] 
           
print('The average weight of a cat is ', round(sum(cat_weights) / len(cat_weights), 2))
