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

profit = 0


def is_resource_sufficient(order_ingredients):
    """function to check whether the ingredients are sufficient or not."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, not enough {item}")
            return False

        return True


def process_coins():
    """returns the total money calculated from number of coins given."""
    print("Please insert your coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01

    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or return False otherwise."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is change: ${change}")

        global profit
        profit += drink_cost
        return True

    else:
        print("not enough money, refunding now...")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕️, Have a nice day!")


is_on = True
while is_on:
    customer_choice = input("What would you like? (espresso☕️/latte🧋/cappuccino︎☕️🍶)").lower()
    if customer_choice == 'off':
        is_on = False

    elif customer_choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${profit} ")

    else:
        drink = MENU[customer_choice]
        # print(drink)
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(customer_choice, drink['ingredients'])
