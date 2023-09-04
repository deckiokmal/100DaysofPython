# Who will pay the meal today

import random

# split() string to a list
data = input("Give the names, seperated by comma: ")
newlist = data.split(", ")

# count item on the list
x = len(newlist) - 1
# generate random integer base on count of item
who_will_pay = random.randint(0, x)

# Give the value who will pay form the list
person_pay = newlist[who_will_pay]
print(f"{person_pay} will pay the meal today.")

# choice() method
person_pay = random.choice(newlist)
print(f"{person_pay} will pay the meal today.")
