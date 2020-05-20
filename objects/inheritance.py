# Wizard & Archer class will inherit the sign_in function from the user class
# by passing it in as a parameter


class User():
    def sign_in(self):
        print('Logged In')

# Subclasses or derived class of User
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    # example of Polymorphism, same method name but different output
    def attack(self):
        print(f'Attacking with power of {self.power}')

# Subclasses or derived class of User
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    # example of Polymorphism, same method name but different output
    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

wizard1.attack()
archer1.attack()

archer1.sign_in()

# Everything in Python is an object, inherits from the base Object class
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))

# Polymorphism in action
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)
