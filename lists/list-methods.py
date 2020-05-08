basket = [1, 2, 3, 4, 5]

# This will print 5, doesn't start at 0
print(len(basket))

# Adding methods

# Append, Insert & Extend adds a new list in place, doesn't produce new result
basket.append(100)

new_list = basket

print(basket)
print(new_list)

# First argument is position, second is value to add
basket.insert(4, 50)

print(basket)

# removing

# Pop removes the last item from a list and returns it in a variable
basket.pop()

# Searches for a specific value and removes if it is found
basket.remove(50)

print(basket)

# Removes all items from the list
basket.clear()

more_shit = ["a", "b", "z", "d", "e", "x", "g", "p"]

# *in* keyword returns bool if item is in list / string
print("c" in more_shit)
print("i" in "I am a goatherding sasquatch")

print(more_shit.count("c"))

# Sort method doesnt modify array, sorted() function creates a new one
more_shit.sort()
print(sorted(more_shit))

print(more_shit)

# .copy() is another way to literally copy a list

# Reverse the items in place - does NOT sort
more_shit.reverse()

# Create mind map with all of these items!
