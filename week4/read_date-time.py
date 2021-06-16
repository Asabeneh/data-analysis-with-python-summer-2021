f = open('./sample.txt')
lines = f.read().splitlines()
print(lines)
from datetime import datetime
for line in lines:
    date_string = line.split('date')[1].strip()
    print(date_string)
    time_object = datetime.strptime(date_string, "%B %d, %Y %H:%M")
    print(time_object)
f.close()

with open('./donald.txt') as f:
    print(f.read())
    