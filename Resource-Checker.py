#Storage checker
print("How many ml of water does the coffe machine have?")
water = int(input().strip())
print("How many ml of milk does the coffee machine have?")
milk = int(input().strip())
print("How many grams of coffee beans does the coffee machine have?")
coffee_beans = int(input().strip())
print("How many cups of coffee (do you need?")
coffee_cups = int(input().strip())

needed_water = coffee_cups * 200
needed_milk = coffee_cups * 50
needed_beans = coffee_cups * 15

maximum_resources = [water // 200, milk // 50, coffee_beans // 15]
maximum_cups = min(maximum_resources)

if maximum_cups == coffee_cups:
    print("Yes, I can make that amount of coffee.")
elif maximum_cups <= coffee_cups:
    print("No, I can only make",maximum_cups,"cups of coffee." if maximum_cups > 1 else "cup of coffee.")
elif maximum_cups >= coffee_cups:
    print("Yes, I can make that amount of coffee. I could even make",maximum_cups - coffee_cups,"more cups.")
