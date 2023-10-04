
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

cost_in_report = 0
update_resource = True


def is_resource_sufficient(choice):
    """ Check if resources are sufficient """
    global resources
    global update_resource

    water = MENU[choice]["ingredients"]["water"]

    if choice == "espresso":
        milk = 0
    else:
        milk = MENU[choice]["ingredients"]["milk"]

    coffee = MENU[choice]["ingredients"]["coffee"]
    cost = MENU[choice]["cost"]

    if water > resources["water"]:
        if milk > resources["milk"] and coffee > resources["coffee"]:
            print("Sorry there is not enough water, milk and coffee.")
        elif milk > resources["milk"]:
            print("Sorry there is not enough water and milk.")
        elif coffee > resources["coffee"]:
            print("Sorry there is not enough water and coffee.")
        else:
            print("Sorry there is not enough water.")
    elif milk > resources["milk"]:
        if coffee > resources["coffee"]:
            print("Sorry there is not enough milk and coffee.")
        else:
            print("Sorry there is not enough milk.")
    elif coffee > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        take_coins_decide_price(cost, choice)
        if update_resource:
            update_resources(water, milk, coffee, cost)


def take_coins_decide_price(cost, choice):
    """Ask for coins and check whether money is enough or not"""
    global update_resource
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    value_of_coins = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)

    remaining_amount = value_of_coins - cost

    if remaining_amount >= 0:
        print(f"Here is ${remaining_amount} in change.")
        print(f"Here is your {choice} ☕. Enjoy!")
        update_resource = True
    elif remaining_amount < 0:
        print("Sorry that's not enough money. Money refunded.")
        update_resource = False


def update_resources(water, milk, coffee, cost):
    """Update the resources available"""
    global cost_in_report
    global resources
    updated_water = resources["water"] - water
    updated_milk = resources["milk"] - milk
    updated_coffee = resources["coffee"] - coffee
    cost_in_report += cost

    resources = {
        "water": updated_water,
        "milk": updated_milk,
        "coffee": updated_coffee,
    }


def choose_drink():

    should_continue = True

    while should_continue:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            is_resource_sufficient(choice)
        elif choice == 'report':
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${cost_in_report}')
        elif choice == 'off':
            should_continue = False


choose_drink()



