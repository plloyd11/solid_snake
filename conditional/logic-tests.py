print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# keyword is - essentially === in JS, SUPER strict equality checker
print('------------------')

print(True is True)
print('1' is '1')
print([] is 1)
print(10 is 10)
print([] is [])  # Created in a new location in memory, will never be equal

# The is keyword is used to test if two variables refer to the same object.
# The test returns True if the two objects are the same object.
# The test returns False if they are not the same object, even if the two objects are 100 % equal.
# Use the == operator to test if two variables are equal
