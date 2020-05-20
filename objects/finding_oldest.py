# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats


booger = Cat('Booger', 12)
aria = Cat('Aria', 10)
lucy = Cat('Lucy', 15)

# 2 Create a function that finds the oldest cat


def oldest(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The oldest cat is {oldest(booger.age, aria.age, lucy.age)} years old.')
