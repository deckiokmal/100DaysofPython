from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_coffee = CoffeeMaker()
my_money = MoneyMachine()


is_on = True
while is_on:
    user_input = input(f"Kopi apa yang ingin anda pesan? {my_menu.get_items()}: ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        my_coffee.report()
        my_money.report()
    else:
        drink = my_menu.find_drink(user_input)
        if my_coffee.is_resource_sufficient(drink) and my_money.make_payment(
            drink.cost
        ):
            my_coffee.make_coffee(drink)
