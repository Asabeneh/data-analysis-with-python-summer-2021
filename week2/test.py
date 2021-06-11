import matplotlib.pyplot as plt
import requests
import numpy as np
from pprint import pprint

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats = response.json()

def cal_life_span (cat):
    return (float(cat['life_span'].split()[0]) + float(cat['life_span'].split()[2])) / 2
def cal_weight (cat):
    return (float(cat['weight']['metric'].split()[0]) + float(cat['weight']['metric'].split()[2])) / 2

cat_weights = list(map(lambda cat:(float(cat['weight']['metric'].split()[0]) + float(cat['weight']['metric'].split()[2])) / 2, cats))
print('The average weight of a cat is ', round(sum(cat_weights) / len(cat_weights), 2))
pprint(cats[0])

countries = [{'country': cat['origin'], 'weight':cal_weight(cat), 'life_span':cal_life_span(cat)} for cat in cats]
# set_countries = set(countries)
# countries_dict = {}
# for c in set_countries:
#     countries_dict[c] = len(list(filter(lambda x: x ==c, countries)))
# pprint(countries_dict)
# x = countries_dict.keys()
# y = countries_dict.values()
# plt.bar(x, y)
# plt.xticks(rotation=45)
# plt.title('Cat Breeds')
# plt.xlabel('Countries')
# plt.ylabel('Number of cats')
# plt.margins(x=0)
# plt.show()
pprint(countries)
locations = list(map(lambda x:x['country'], countries))
print('locations', locations)
weights = list(map(lambda x:x['weight'], countries))
years= list(map(lambda x:x['life_span'], countries))

X_axis = np.arange(len(locations))
# plt.bar(X_axis - 2, weights, label = 'years')
# plt.bar(X_axis + 2, years,label = 'years')

# plt.xticks(X_axis, locations)
# plt.xticks(rotation=45)
# plt.title('Life Span of Cats')
# plt.xlabel('Countries')
# plt.ylabel('Number of years')
# plt.margins(x=0)
# plt.show()

import numpy as np 
import matplotlib.pyplot as plt 
  

Ygirls = [10,20,20,40]
Zboys = [20,30,25,30]
  
X_axis = np.arange(len(locations))
  
plt.bar(X_axis - 0.2, weights, 0.4, label = 'Weight')
plt.bar(X_axis + 0.2, years, 0.4, label = 'Life Span')
plt.xticks(rotation=45)
plt.xticks(X_axis, locations)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group")
plt.legend()
plt.show()
    