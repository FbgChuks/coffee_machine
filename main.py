


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





# Initial resources
water = 300
milk = 200
coffee = 100
money = 0.0



while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money:.2f}")
    elif choice in MENU:
        drink = MENU[choice]
        required_water = drink["water"]
        required_milk = drink["milk"]
        required_coffee = drink["coffee"]
        cost = drink["cost"]

        # Check resources
        if water < required_water:
            print("Sorry there is not enough water.")
        elif milk < required_milk:
            print("Sorry there is not enough milk.")
        elif coffee < required_coffee:
            print("Sorry there is not enough coffee.")
        else:
            # Proceed to payment
            print(f"Please insert coins. The cost is ${cost:.2f}.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))

            total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

            if total < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                # Add cost to money, give change, deduct resources
                money += cost
                change = total - cost
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                water -= required_water
                milk -= required_milk
                coffee -= required_coffee
                print(f"Here is your {choice}. Enjoy!")
    else:
        print("Invalid choice. Please try again.")