menu = {
    "fries": 3.00,
    "popcorn": 4.00,
    "nachos": 2.00,
    "pizza": 5.00,
    "coke": 2.00,
    "lemonade": 1.00,
}
item = []
total = 0
print("------ MENU ------")
for keys, values in menu.items():

    print(f"{keys:10}: ${values:.2f}")

print("------------------")
print("Type exit to finish order")
while True:
    food = input("Choose what you want: ")
    if food.lower() == "exit":
        break

    elif menu.get(food) is not None:
        item.append(food)
print("--------- YOUR ORDER ---------")       
for food in item:
    total += menu.get(food)
    print(food, end=" ")


print()
print(f"Total price is: ${total:.2f}")
