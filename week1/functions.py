def print_full_name(first_name, last_name):
    full_name = first_name +  ' ' + last_name
    return full_name

print(print_full_name('John', 'Doe'))
print(print_full_name('Asabeneh', 'Yetayeh'))

def calculate_weight(mass, gravity = 9.81):
    weight = mass * gravity
    return weight

print(calculate_weight(75))
print(calculate_weight(75, 1.62))


linear_eqn = lambda x : 2 * x + 5
print(linear_eqn(2))
