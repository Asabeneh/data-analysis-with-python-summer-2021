# Descriptive statistics

## Write a script that calculate the max, min,  mean, median, standard deviation, range, mode, percentile ? weight | life_span of the cats from the cats api

#[1,2, 1, 3,6, 3,5, 3, 4]
# [1,1, 2, 3,3,3 4,5,6]

import requests
from pprint import pprint

url = 'https://api.thecatapi.com/v1/breeds'

def fetch_api_data(url):
    response = requests.get(url)
    data = response.json()
    return data

cats = fetch_api_data(url)


def format_weight(cat):
    return (eval(cat['weight']['metric'].replace('-', '+')))/2
            
weights = [format_weight(cat) for cat in cats]
pprint(weights)

# mean => [2, 1, 3, 4, 2] => (2 + 1 + 3 + 4 + 2) / 5

nums = [2, 1, 3, 4, 2]

def cal_mean(lst):
    total = sum(weights)
    n = len(weights)
    average = total / n
    return round(average, 2)

print(cal_mean(weights))

# median => [2, 1, 3, 4, 2] => (2 + 1 + 3 + 4 + 2) / 5
# sorting =>  [1, 2, 2, 3, 4] =>  n / 2 = 5 // 2 = math.floor(2.5)
# sorting =>  [1, 2, 2, 3, 4, 5] =>  n / 2 = 6//2 => 3  => (n/2), (n/2) - 1

def cal_median (lst):
    n = len(lst)
    sorted_list = sorted(lst)
    if n % 2 == 0:
        first_index  = int(n / 2)
        second_index = first_index - 1
        return (sorted_list[first_index] + sorted_list[second_index]) / 2
    else:
        index = n // 2
        return sorted_list[index]
print('median', cal_median([2, 1, 3, 4, 2]))
print('median', cal_median([1, 2, 2, 3, 4, 5]))
print('meaian of cats weight', cal_median(weights))
        
# standard variation => [2, 1, 3, 4, 2] => (2 + 1 + 3 + 4 + 2) / 5
# Calculate mean
#  ((x1 - mean)**2 +  (x2 - mean)**2 + (xn-mean))/n


def cal_stdev(lst):
    mean = cal_mean(lst)
    n = len(lst)
    total = 0
    for x in lst:
        total += (x - mean) ** 2
    stdev = (total / n ) ** 0.5
    return round(stdev, 2)
print(cal_stdev(weights))

def cal_varience(lst):
    varience =  cal_stdev(lst) ** 2
    return round(varience, 2)

print(cal_varience(weights))

def cal_range(lst):
    # sorted_lst = sorted(lst)
    # mx = sorted_lst[-1]
    # mn = sorted_lst[0]
    # return mx - mn
    return max(lst) - min(lst)

print('The range of cats weight:', cal_range(weights))
print('Max of weights', max(weights))
print('Min of cats weight', min(weights))

# data => [2, 1, 3, 4, 2] 
# sorting =>  [1, 2, 2, 3, 4]
# data   freq
# 1      1
# 2      2
# 3      1
# 4      1

def cal_mode(lst):
    freq_table = {}
    for x in  lst:
        if x not in freq_table:
            freq_table[x] = 1
        else:
            freq_table[x] = freq_table[x] + 1
    sorted_value = sorted(freq_table.items(), key=lambda x:x[1], reverse=True)
    return sorted_value[0]
print('mode', cal_mode(weights))

def find_freq_table(lst, n = 10):
    freq_table = {}
    for x in  lst:
        if x not in freq_table:
            freq_table[x] = 1
        else:
            freq_table[x] = freq_table[x] + 1
    sorted_value = sorted(freq_table.items(), key=lambda x:x[1], reverse=True)
    return sorted_value[:n]


freq_table = {}
for x in  weights:
    if x not in freq_table:
        freq_table[x] = 1
    else:
        freq_table[x] = freq_table[x] + 1
sorted_value = sorted(freq_table.items(), key=lambda x:x[1], reverse=True)
print(sorted_value)

x = []
y  = []

for k, v in sorted_value:
    x.append(k)
    y.append(v)
    

import matplotlib.pyplot as plt

plt.bar(x, y, color='coral', width = 0.35)
plt.xlabel('Weight in Kg')
plt.ylabel('Count')
plt.title('Cats weight')
plt.savefig('./cats-weight-freq_table.png')
plt.show()


        


    


    

        
    


    


