#Amount of resources before making x amount of coffee:

#Random start amount for test
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550

print("The coffee machine has:")
print(water, "of water")
print(milk, "of milk")
print(coffee_beans, "of coffee beans")
print(disposable_cups, "of disposable cups")
print(money, "of money")

print()

#Action selector
print("Write action (buy, fill or take):")
action = str(input())

#Buy coffee
if action == "buy":
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    disposable_cups -= 1
    buy_option = int(input())
    if buy_option == 1:
        water -= 250
        coffee_beans -= 16
        money += 4
    elif buy_option == 2:
        water -= 350
        coffee_beans -= 20
        milk -= 75
        money += 7
    elif buy_option == 3:
        water -= 200
        coffee_beans -= 12
        milk -= 100
        money += 6

#Fill machine with resources
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

#Take money
elif action == "take":
    print("I gave you $", money)
    money -= money

print()

#Amount of resources afterwards:
print("The coffee machine has:")
print(water, "of water")
print(milk, "of milk")
print(coffee_beans, "of coffee beans")
print(disposable_cups, "of disposable cups")
print(money, "of money")





