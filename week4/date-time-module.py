def generate_date_time():
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    month = now.month
    day = now.day
    year = now.year
    hour_minute = f'{hour}:{minute}'
    m = ''
    if month < 10:
        m = '0' + str(month)
    print(f'{day}/{m}/{year}')
    print(f'{day}-0{month}-{year}')

    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    long_time_format = f'Today is {months[month -1]} {day}, {year}'
    return long_time_format, hour_minute

print(generate_date_time())

from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year.year)

now = datetime.now()
t = now.strftime("%B %d, %Y %I:%M %p")
print(t)

date_string = "5 December, 2019"
time_object = datetime.strptime(date_string, "%d %B, %Y")
print(time_object)

from datetime import date
d = date(2020, 1, 1)
print(d)
print('Today:', d.today())

from datetime import time

t = time()
print(t)
b = time(10, 30, 50)
print(b)

c = time(minute=30, hour=10, second=50)
print(c)

today = date(year=2021, month=6, day=16)
new_year = date(year=2022, month=1, day=1)
print(new_year - today)

try:
    print('I am happy to run.')
except Exception as e:
    print(e)
else:
    print('i GO WITH THE TRY')
finally:
    print('I will be executed no matter what')

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
print(sum_of_five_nums(*lst))  # 15
firstname, lastname, age = ('Asabeneh','Yetayeh', 250)

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers) 

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw)
print(rest)

def unpacking_person_info(name, country, city, age):
    print(name)
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) 

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

print('Countries I like the most:')
for i, c in enumerate(countries):

    print(f'{i + 1}-{c}')
    
odds = list( range(1, 102, 2))
evens = list(range(0, 101, 2))
print(len(odds), len(evens))

for i in zip(evens, odds, odds):
    print(i)
