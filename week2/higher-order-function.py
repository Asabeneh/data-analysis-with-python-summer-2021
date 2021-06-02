# map, filter, reduce

nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]

# new_list =  [i ** 2 for i in nums]
# print(new_list)

# def map_a_list(lst):
#     new_lst = []
#     for i in lst:
#         new_lst.append(i ** 2)
#     return new_lst

# print(map_a_list(nums))


# def make_square(x):
#     return x ** 2

# new_lst = list(map(make_square, nums))
# print(new_lst)

# countries = ['Finland','Sweden','Denmark','Norway','Iceland']

# countries_upper = map(lambda country : [country, country.upper(),country.upper()[0:3]], countries)
# print(list(countries_upper))
# # Filter

# evens = filter(lambda x : x % 2 == 0, nums)
# print(list(evens))
# odds = filter(lambda x : x % 2 != 0, nums)
# print(list(odds))

# countries_with_land = filter(lambda x: 'land' in x, countries)
# print(list(countries_with_land))

# countries_without_land = filter(lambda x: 'land' not in x, countries)
# print(list(countries_without_land))
# # Reduce

# from functools import reduce

# total = reduce(lambda a, b : a + b, nums)
# print(total)

## sort is a method => mutate the original data
## sorted is a builtin functions => this does not mutate the original data

nums = [-2, 4, -5, 9, 10, 3, 5, 8, 0]

# nums1 = nums
# nums1.sort(reverse=True) 
# print(nums1)
# print(nums)
sorted_nums = sorted(nums, reverse=True)
print(nums)
print(sorted_nums)

# Importing modules