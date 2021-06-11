import matplotlib.pyplot as plt
import requests
import numpy as np
from pprint import pprint
import seaborn as sn
plt.style.use('ggplot')

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

def create_cat_life_span_graph():
    countries = [{'country': cat['origin'], 'weight':cal_weight(cat), 'life_span':cal_life_span(cat)} for cat in cats]
    locations = list(map(lambda x:x['country'], countries))
    print('locations', locations)
    weights = list(map(lambda x:x['weight'], countries))
    years= list(map(lambda x:x['life_span'], countries))

    plt.bar(locations, years, color='royalblue', alpha=0.9)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.title('Life Span of Cats and their Country of Origin')
    plt.xlabel('Countries')
    plt.xticks(size = 10)
    plt.ylabel('Number of years')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.margins(x=0)
    plt.savefig('./life_span.png')
    plt.show()
    
# create_cat_life_span_graph()

def create_cats_weight_graph():
    countries = [{'country': cat['origin'], 'weight':cal_weight(cat), 'life_span':cal_life_span(cat)} for cat in cats]
    locations = list(map(lambda x:x['country'], countries))
    print('locations', locations)
    weights = list(map(lambda x:x['weight'], countries))
    
    plt.bar(locations, weights, color='coral', alpha=0.9)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.title('Weight of Cats and their Country of Origin')
    plt.xlabel('Countries')
    plt.xticks(size = 10)
    plt.ylabel('Mass in Kg')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.margins(x=0)
    plt.savefig('./weight.png')
    plt.show()

# create_cats_weight_graph()


def create_countries_graph():
    countries = [{'country': cat['origin'], 'weight':cal_weight(cat), 'life_span':cal_life_span(cat)} for cat in cats]
    locations = list(map(lambda x:x['country'], countries))
    locations_set = set(locations)
    countries_dict = {}
    for c in locations_set:
        countries_dict[c] = len(list(filter(lambda x: x['country'] == c, countries)))
    
    x = list(countries_dict.keys())
    y = countries_dict.values()
    import os
    plt.bar(x, y, color='#ff6361', alpha=0.9)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.title('Number of cat breeds in different countries')
    plt.xlabel('Countries')
    plt.xticks(size = 10)
    plt.ylabel('Number of cat breeds')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.margins(x=0)
    plt.savefig('./breeds.png')
    plt.show()
    
create_countries_graph()

def pie_chart():
    countries = [{'country': cat['origin'], 'weight':cal_weight(cat), 'life_span':cal_life_span(cat)} for cat in cats]
    locations = list(map(lambda x:x['country'], countries))
    locations_set = set(locations)
    countries_dict = {}
    for c in locations_set:
            countries_dict[c] = len(list(filter(lambda x: x['country'] == c, countries)))
    
    x = list(countries_dict.keys())
    y = countries_dict.values()

    explode = len(x)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(y,  labels=x, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('./breeds-pie-chart.png')
    plt.show()
pie_chart()