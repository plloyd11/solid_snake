# Reversing

basket = ["a", "x", "b", "c", "d", "e", "d"]

basket.sort()
basket.reverse()

# Another way to reverse using slicing
print(basket[::-1])
print(basket)

print(list(range(1, 100)))

# Combining a list into a string
sentence = " ".join(["hi", "my", "name", "is", "bernie"])

print(sentence)

# List unpacking
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
