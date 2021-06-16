import os
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

with open('./test.txt', 'a') as f:
    f.write('something')
os.remove('./test.txt')
    # for m in months:
    #     f.write(f'I work in {m}.\n')
     
     
   
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)