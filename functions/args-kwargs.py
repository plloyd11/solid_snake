# * in front of parameter means it can accept any number of positional arguments
# kwargs returns item in a dictionary


def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 6, 7, 8, num1=5, num2=60))
