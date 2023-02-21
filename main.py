from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_available = Menu()
coffee_maker = CoffeeMaker()
process_coin = MoneyMachine()

is_machine_on = True

while is_machine_on:

    order_drink = input(f"What would you like? ({drink_available.get_items()}):").lower()

    if order_drink == "off":
        is_machine_on = False
    elif order_drink == "report":
        coffee_maker.report()
        process_coin.report()
    else:
        drink_dicitionary = drink_available.find_drink(order_drink)
        if coffee_maker.is_resource_sufficient(drink_dicitionary):
            if process_coin.make_payment(drink_dicitionary.cost):
                coffee_maker.make_coffee(drink_dicitionary)