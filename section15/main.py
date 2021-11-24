import data

money = 0


# todo, process coins
def check_coins(drink):
    enough = False
    price = data.MENU[drink]["cost"]
    print("Throw in your money:")
    quarters = int(input("Amount of quarters: ")) * 0.25
    dimes = int(input("Amount of dimes: ")) * 0.10
    nickles = int(input("Amount of nickles: ")) * 0.05
    pennies = int(input("Amount of quarters: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    # todo, check successful transaction
    if total > price:
        print("Enough money!")
        enough = True
        change = total - price
        print(f"Your change = {change}")
        global money
        money += price
        print("Transaction succesful")
    else:
        print("Not enough funds")
    return enough


# todo, check resources sufficient for drink
def check_ingredients(drink):
    print("Checking ingredients...")
    enough = False
    option = data.MENU[drink]["ingredients"]
    water_left = data.resources["water"]
    milk_left = data.resources["milk"]
    coffee_left = data.resources["coffee"]
    if water_left < option["water"] or milk_left < option["milk"] or coffee_left < option["coffee"]:
        print("Not enough ingredients.")
        enough = False
    else:
        print("Enough ingredients!")
        data.resources["water"] -= option["water"]
        data.resources["milk"] -= option["milk"]
        data.resources["coffee"] -= option["coffee"]
        enough = True
    return enough


# todo, make coffee (edit resources and add money to total)
def make_drink(drink):
    print(f"Making your {drink}!")
    print(f"Enjoy your {drink}!")


def main():
    turned_off = False
    print("Let's make some coffee!")
    while not turned_off:

        print("Options:\n1. Espresso\n2. Latte\n3. Cappuccino\n4. Report")
        choice = input("What would you like?").lower()
        if choice == "espresso" or choice == "latte" or choice == "cappuccino":
            # check_ingredients(choice)
            ingredients = check_ingredients(choice)
            if ingredients:
                coins = check_coins(choice)
                if coins:
                    make_drink(choice)
                else:
                    print("Not enough money to make your drink")
            else:
                print("Not enough ingredients to make your drink.")
        elif choice == "report":
            # todo, print report(ingredients left and money)
            for subject in data.resources:
                print(f"{subject}: {data.resources[subject]}")
            print(f"money: {money}")
        elif choice == "off":
            print("Turning off...")
            turned_off = True


if __name__ == '__main__':
    main()