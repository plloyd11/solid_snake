# Immutable Lists

my_tuple = (1, 2, 3, 4, 5)

# Errors - think of a const in JS but as a list
# my_tuple[1] = "z"

print(5 in my_tuple)

# Faster than a normal list since they cant change

# .items() method returns a tuple from a dict

user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}

print(user.items())

# Has only two methods: Count and Index

print(my_tuple.index(5))
print(my_tuple.count(3))
