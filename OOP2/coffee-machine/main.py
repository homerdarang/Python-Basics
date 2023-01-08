from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()




make_coffee = True

while make_coffee:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        make_coffee = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drinks = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drinks) and money_machine.make_payment(drinks.cost):
            coffee_maker.make_coffee(drinks)


