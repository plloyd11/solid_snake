# Looping!
sick_bands = ['Gorguts', 'Morbid Angel', 'Defeated Sanity']

for band in sick_bands:
    print(f'Good call, motherfucker! {band} is fuckin\' sweet!')

user = {
    "name": 'Golem',
    "age": 5006,
    "can_swim": False
}

# Things that are iterable - list, dictionary, tuple, set, string

# Iterated - one by one check of each item in the collection

# dictionary methods for looping:

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# Print each key - value shorthand

for key, value in user.items():
    print(key, value)
