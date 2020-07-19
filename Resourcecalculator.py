print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!"""
)

#Amount of cups of coffee needed
print("Write how many cups of coffee you'll need:")
coffee_cups = int(input())

#This is the part that calculates the ingredients
print("For",coffee_cups,"cups of coffee you'll need:")

#Water:
print(coffee_cups * 200,"ml of water")

#Milk:
print(coffee_cups * 50,"ml of milk")

#Coffee beans:
print(coffee_cups * 15,"g of coffee beans")

print()

