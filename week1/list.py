# collection of ordered items

nums = [1, 2, 3, 4]
print(nums)
print(len(nums))
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
lastIndex = len(nums) - 1
print(nums[lastIndex])
print(nums[3])
print(nums[-1])
print(nums[-4])
nums[0] = 100
print(nums)
nums[-1] = 40
print(nums)
nums.pop()
print(nums)
nums.append(900)
nums.append(500)
print(nums)
nums.extend([8,7,9, 200, 300])
print(nums)

numbers = list(range(1,1001, 100))
print(numbers)
print(list('Python'))


fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
# list of vegetables
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
fruits_and_vegs = fruits + vegetables
print(fruits_and_vegs)

fruits_and_vegs = fruits + vegetables
nums = [1, 2, 3, 4, 5, 6]
one, two, three, *rest = nums
print(one)
print(rest)
print(vegetables[0:2])
print(vegetables[1:4])

print('Ethiopia' in countries)
print('Finland' in countries)
print('thon' in 'Python')
nums.insert(3, 7)
print(nums)
# countries.remove('Estonia')
# print(countries)
# del countries[1:3]
print(countries)
nums = [1, 2, 2, 3, 4, 5,2]
print(nums.count(2))
nums.reverse()
print(nums)

countries.sort(reverse=True)
print(countries)