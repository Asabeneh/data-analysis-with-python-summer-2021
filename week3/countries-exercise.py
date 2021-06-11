import requests
import matplotlib.pyplot as plt
from functools import reduce

from pprint import pprint


url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
data = response.json()
# print(len(data))
# pprint(data[:2])

populations = [[c['name'], c['population']] for c in data]
# pprint(populations[:3])

total = reduce(lambda a, b: a + b, list(map(lambda x: x[1], populations)))
print(total)

def create_countries_bar_graph():
    # sort, sorted
    populations_sorted = sorted(populations,key= lambda x:x[1], reverse=True)
    # print(populations_sorted)
    most_populated_countries = populations_sorted[:10]
    print(most_populated_countries)
    x = [c[0] for c in most_populated_countries]
    y = [c[1] for c in most_populated_countries]
    colors =[
    "#8111d8",
    "#c23323",
    "#960a4a",
    "#5e3ebf",
    "#c7a8ff",
    "#8bfba1",
    "#bd51e3",
    "#8339c6",
    "#104675",
    "#947ac0"
]
    plt.bar(x, y, color=colors)
    plt.xlabel('Countries')
    plt.ylabel('Populations')
    plt.title('Ten most populated countries in the world')
    plt.savefig('./ten_most_populated_countries.png')
    plt.show()


# create_countries_bar_graph()

def calc_percentage(n,total):
    return (n / total) * 100

populations_percentage = [[c['name'], c['population'], calc_percentage(c['population'], total )] for c in data]
print(populations_percentage[:10])


populations_sorted = sorted(populations,key= lambda x:x[1], reverse=True)
    # print(populations_sorted)
most_populated_countries = populations_sorted[:10]
populations_percentage = [[c[0], c[1], calc_percentage(c[1], total )] for c in most_populated_countries]
pprint(populations_percentage[:10])






def create_pie_chart ():
    
    populations_sorted = sorted(populations,key= lambda x:x[1], reverse=True)
        # print(populations_sorted)
    most_populated_countries = populations_sorted[:10]
    populations_percentage = [[c[0], c[1], calc_percentage(c[1], total )] for c in most_populated_countries]
    pprint(populations_percentage[:10])
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = [c[0] for c in most_populated_countries]
    sizes =[c[1] for c in most_populated_countries]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    
# create_pie_chart()


# You problem does have any pattern
# You have come with a certain structure
#
scandinavinian_countries = ['Finland', 'Sweden','Denmark','Norway','Iceland']

scandic = [[c['name'],c['population'] ] for c in data if c['name'] in scandinavinian_countries]
print(scandic)
