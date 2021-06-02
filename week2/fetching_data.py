import requests
from pprint import pprint

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats = response.json()
cat_weights = []
for cat in cats:
    first_num = float(cat['weight']['metric'].split()[0])
    second_num = float(cat['weight']['metric'].split()[2])
    num = (first_num + second_num) / 2
    cat_weights.append(num)
print(round(sum(cat_weights) / len(cat_weights), 2))

 
    # cat_weights.append()
pprint(response.json()[0])

