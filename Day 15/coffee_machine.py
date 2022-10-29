"""data for coffee type and cost"""
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
        "cost": 25,
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

amount = 0
is_on = True


def is_resource_sufficient(order_ingredients):
    """checks if there is enough resource and returns 'True' or 'False'"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """take coins from user and returns total"""
    print("Please insert coins")
    total = int(input("How many 1 rupee coins: "))
    total += int(input("How many 2 rupee coins: ")) * 2
    total += int(input("How many 5 rupee coins: ")) * 5
    total += int(input("How many 10 rupee coins: ")) * 10
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns 'True' when payment is accepted otherwise returns 'False' and
    refunds the amount."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        global amount
        amount += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """If everything is ok, then this function will make/print the coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\nMoney: ₹{amount}")
    elif choice in ['espresso', 'latte', 'cappuccino']:
        drink = MENU[choice]

        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
    else:
        print("Wrong input!")
