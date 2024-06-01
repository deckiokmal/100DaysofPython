# Python Object Oriented Programming


# Class
class Car:
    # Attribute
    def __init__(self, speed):
        self.speed = speed

    # Method
    def move(self, a, b):
        return a + b


# Object
toyota = Car(100)
print(toyota)

# Object with Attribute
print(toyota.speed)

# Object with Method
print(toyota.move(1, 2))
