from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cafe_machine = CoffeeMaker()
drinks = Menu()
cash = MoneyMachine()


on = True
while on:

    """Did not have this but this is a good point. adding options variable allows me to print out the available options
    from the coffee machine. this is important for a) the user know actually know what their options are, and b) the 
    potential to increase the available options in the future"""

    options = drinks.get_items()
    coffee = input(f"What kind of coffee would you like? ({options})").lower()

    if coffee == "off":
        on = False
    if coffee == "report":
        cafe_machine.report()
        cash.report()
        #checks if coffee is an option in the string of options += item.name
    elif coffee in drinks.get_items():

        #assigns variable to drink where find_drink searches MenuItem objects in self.menu list
        selected_drink = drinks.find_drink(coffee)

        #calls CoffeeMaker.is_resource_sufficient and passes MenuItem. No .ingredient because expected parameter is Menu Item
        can_make = cafe_machine.is_resource_sufficient(selected_drink)
        if can_make:
            #calls MoneyMachine().make_payment for payment and passes the cost of the MenuItem object as the parameter
            paid = cash.make_payment(selected_drink.cost)
            if paid:
                #calls CoffeeMaker.make_coffee and passes MenuItem. MenuItem provides all information for making coffee
                cafe_machine.make_coffee(selected_drink)
        else:
            on = False

