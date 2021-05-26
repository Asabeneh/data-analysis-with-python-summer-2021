# 
for i in range(0, 10, 2):
    print(i)

country_codes = []  
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
for country in countries:
    country_codes.append([country.upper(), country.upper()[0:3]])
    
print(country_codes)

total = 0 
for i in range(0, 101, 2):
    total = total + i
print(total)

count = 10
while count >= 0:
    print(count)
    count = count  - 1