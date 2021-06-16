import re 

# match, search, findall
string = 'You love Python but I love JavaScript. Love is something you should give to everyone.What do you want?  A potato or tomato. I go for potato.'
txt = '''I am teacher and  I love teaching. There is nothing as rewarding as educating and empowering people. I found teaching more interesting than any other jobs. Does this motivate you to be a teacher? Love is powerfull'''
new_string = re.sub(r'love|Love', 'hate', string)
print(new_string)


