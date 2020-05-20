# OOP


class PlayerCharacter:
    # Class Object Attribute (not dynamic - STATIC)
    membership = True

    def __init__(self, name, age):
        if (self.membership):
            self._name = name  # class attribute - DYNAMIC and specific to each individual object
            self._age = age

    def shout_name(self):
        print(f'What the fuck is good, {self._name}'.upper())

    # Can be called without actually instantiating a new instance
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Bernie', 23)

player1.shout_name()
