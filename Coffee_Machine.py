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


money = 0
is_on = True

def is_resource_sufficient(order_ingredients):
    """This function calculates if the machine has the resources to make the coffee."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
        else:
            resources[item] -= order_ingredients[item]
    return True

while is_on == True:

    request = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if request == "off":
        print("Powering off.")
        is_on = False

    elif request == "report":
         print(f"Water: {resources['water']}ml")
         print(f"Milk: {resources['milk']}ml")
         print(f"Coffee: {resources['coffee']}g")
         print(f"Money: ${money}")

    elif request in MENU:
        drink = MENU[request]
        if is_resource_sufficient(drink["ingredients"]):

            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))

            initial_coins = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
            total_coins = round(initial_coins, 2)

            if total_coins >= drink["cost"]:
                money += total_coins

                if total_coins > drink["cost"]:
                    change = total_coins - drink["cost"]

                    if change >= money:
                        print("Insufficient change in machine. Please contact the manager for assistance.")
                    else:

                        print(f"Here is your change: {change}")
                        money -= change


                print("Enjoy your coffee.")
            else:
                print("Insufficient coins. Money refunded.")

    else:
        print(f"Invalid input. Please try again.")



