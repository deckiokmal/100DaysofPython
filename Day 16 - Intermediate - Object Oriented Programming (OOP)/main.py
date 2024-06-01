# Object Oriented Programming memiliki Atribute (Variable) dan Method (Function)
# Atribute dan Method tersebut berada didalam sebuat Class (BluePrint)

# BluePrint terdiri dari Class dan Object, dimana Object dibuat dari Class
# car = Object dan CarBluePrint() adalah Class. Penulisan nama Class diawali dengan huruf Capital (Pascal Case)

# Constructing Object
# car = CarBluePrint()  # ini adalah cara bagaiamana Costructing Object dari Class

# # Attribute Object
# car.speed = 100
# car.fuel = 25

# # Method Object
# car.stop()


################################################################################
from turtle import Turtle, Screen

tony = Turtle()  # membuat Object tony dengan Class Turtle()
print(tony)
tony.shape("turtle")
tony.color("red", "green")
tony.position()
tony.forward(25)
tony.position()
tony.forward(25)
tony.position()

my_screen = Screen()  # membuat Object my_screen dengan Class Screen()
print(my_screen.canvheight)  # menggunakan Attribute
my_screen.exitonclick()  # menggunakan Method
