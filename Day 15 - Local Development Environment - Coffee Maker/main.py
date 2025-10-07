MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def money_paid(drink):
    coins = {"quarter": .25, "dime": .10, "nickel": .05, "penny": .01}
    coin_count = {}
    total = 0

    print("Please insert coins")
    for coin in coins:
        coin_count[coin] = int(input(f"How many {coin}s?: "))

    for coin in coin_count:
        total += coin_count[coin]*coins[coin]
    change = total - MENU[drink]["cost"]

    return round(change, 2), MENU[drink]["cost"]

def is_enough(ingredients, available_resources):
    for ingredient in ingredients:
        if available_resources[ingredient] < ingredients[ingredient]:
            return False
        else:
            available_resources[ingredient] -= ingredients[ingredient]
    return True

profit = 0
coffeeing = True
while coffeeing:
    coffee = input("What would you like? (espresso/latte/cappuccino)").lower()


    if coffee in MENU:
        if is_enough(MENU[coffee]["ingredients"], resources):
            give_back, coffer = money_paid(coffee)
            profit += coffer
            if give_back >= 0:
                print(f"Keep the change, ${give_back}, ya filthy animal")
                print(f"Here's your {coffee} ☕ Enjoy!")
                coffeeing = True
            else:
                print("Getcho paper up!")
                coffeeing = False
        else:
            print("Sorry theres not enough resources")
            coffeeing = False
    elif coffee == "report":
        for resource in resources:
            if resource == "coffee":
                unit = "g"
            else:
                unit = "ml"
            print(f"{resource}: {resources[resource]} {unit}")
        print(f"Money: ${profit}")
        coffeeing = True
    else:
        print("You broke the coffee maker!")
        coffeeing = False