cool_shit = {"basket": [1, 2, 3], "greet": "hello!"}

# See if something exists in a dict

print(cool_shit.get("basket"))

# Check to see if age key exists, if not set the default value to 55
print(cool_shit.get("age", 55))

# Dict methods for checking existence
print("basket" in cool_shit.keys())  # True then false
print("hello" in cool_shit.values())

# Empty the dict

print(cool_shit.clear())

# Copy a dict
print(cool_shit.copy())

# Update or add a new key / value pair
print(cool_shit.update({"age": 55}))
