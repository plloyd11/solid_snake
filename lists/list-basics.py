shopping_cart = ["notebooks", "sunglasses", "toys", "grapes"]

print(shopping_cart[0])
print(shopping_cart[1])

# List slicing - creates new copy of the list
print(shopping_cart[0:2])
print(shopping_cart[0::2])

# Strings are immutable, but lists are mutable

shopping_cart[0] = "laptop"

# Trick to copy lists

new_cart = shopping_cart[:]
