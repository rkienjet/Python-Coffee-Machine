#Amount of resources before making x amount of coffee

water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550

def Resources():
    print("The coffee machine has:")
    print(water, "ml of water")
    print(milk, "ml of milk")
    print(coffee_beans, "grams of coffee beans")
    print(disposable_cups, "disposable cups")
    print("$", money)

while True:
    print("Write action (buy, fill, remaining, take, exit):")
    action = str(input())
    print()
    if action == "exit":
        print("Goodbye!")
        break
    
    elif action == "remaining":
        Resources()
  
    elif action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino. Type 'back' to go back to the main screen:")
        buy_option = input().strip()
        print()
        if buy_option == "back":
            continue
        if buy_option == "1":
            if water < 250 or coffee_beans < 16 or disposable_cups < 1:
                if water < 250:
                    print("Sorry, not enough water!")
                elif coffee_beans < 16:
                    print("Sorry, not enough coffee beans!")
                elif disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
            else:
                disposable_cups -= 1
                print("I have enough resources, making you a coffee!")
                water -= 250
                coffee_beans -= 16
                money += 4
            continue
        elif buy_option == "2":
            if  water < 350 or milk < 75 or disposable_cups < 1:
                if water < 350:
                    print("Sorry, not enough water!")
                elif milk < 75:
                    print("Sorry, not enough milk!")
                elif disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
            else:
                disposable_cups -= 1
                print("I have enough resources, making you a coffee!")
                water -= 350
                coffee_beans -= 20
                milk -= 75
                money += 7
            continue
        elif buy_option == "3":
            if water < 200 or milk < 100 or coffee_beans < 12 or disposable_cups < 1:
                if water < 200:
                    print("Sorry, not enough water!")
                elif milk < 100:
                    print("Sorry, not enough milk!")
                elif coffee_beans < 12:
                    print("Sorry, not enough coffee beans!")
                elif disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
            else:
                disposable_cups -= 1
                print("I have enough resources, making you a coffee!")
                water -= 200
                coffee_beans -= 12
                milk -= 100
                money += 6
            continue

    elif action == "fill":
        print("Write how many ml of water you want to add to the machine:")
        fill_water = int(input())
        print("Write how many ml of milk you want to add to the machine:")
        fill_milk = int(input())
        print("Write how many grams of coffee beans you want to add to the machine:")
        fill_coffee_beans = int(input())
        print("Write how many disposable cups of coffee you want to add to the machine:")
        fill_disposable_cups = int(input())
        water += fill_water
        milk += fill_milk
        coffee_beans += fill_coffee_beans
        disposable_cups += fill_disposable_cups
        print()
        print("New amount of resources:")
        Resources()
        continue

    elif action == "take":
        print("I gave you $", money)
        money -= money
        continue





