"""
Pertanyaan 1:
What will be printed in the console when the following code is run?

DO NOT run the code, just pretend to be a computer.
"""


def a_function(a_parameter):
    a_variable = 15
    return a_parameter


a_function(10)
print(a_variable)


"""
Pertanyaan 2:
What will be printed in the console when the code is run?

DO NOT run the code, just pretend to be a computer.
"""

i = 50


def foo():
    i = 100
    return i


foo()
print(i)

"""
Pertanyaan 3:
What will be printed in the console when the following code is run?

DO NOT run the code, just pretend to be a computer.

Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.

"""


def bar():
    my_variable = 9

    if 16 > 9:
        my_variable = 16

    print(my_variable)


bar()
