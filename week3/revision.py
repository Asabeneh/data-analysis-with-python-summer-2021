
import requests
from pprint import pprint
import matplotlib.pyplot as plt

url = 'https://api.thecatapi.com/v1/breeds'
# get, post, put, delete

respose = requests.get(url)
# print(respose.status_code)
cats = respose.json()
# pprint(data[:2])

nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]

def calc_average_weight(cat):
    first = float(cat['weight']['metric'].split()[0])
    second = float(cat['weight']['metric'].split()[2])
    return (first + second) / 2
    
cat_weights = [calc_average_weight(cat) for cat in cats]
# pprint(cat_weights)

weights = list(map(calc_average_weight, cats))

def calc_average_life_span(cat):
    first = float(cat['life_span'].split()[0])
    second = float(cat['life_span'].split()[2])
    return (first + second) / 2

cats_life_span = [calc_average_life_span(cat) for cat in cats]
# print(cats_life_span)

def calc_mean(data):
    return round(sum(data) / len(data), 2)

# print(f'The mean of cats life span is {calc_mean(cats_life_span)} Kg.')
# print(f'The mean of  cats weight is {calc_mean(weights)} years.',)

x = [-3, -2, -1, 0, 1, 2, 3]
y = [i ** 2 for i in x] # y = x ** 2

print(x)
print(y)

plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Temperature vs Pressure')
plt.show()

# 


