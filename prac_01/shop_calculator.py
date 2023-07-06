num_of_items = int(input("Number of items: "))


while num_of_items < 0:
    print("Invalid number of items!")
    num_of_items = int(input("Number of items: "))


total_cost = 0
for i in range(num_of_items):
    item_price = float(input("Price of item: "))
    total_cost += item_price


# If the total price is over $100. So not equal to 100?
if total_cost > 100:
    discounted_cost = total_cost * 0.1
    total_cost -= discounted_cost


print(f"Total price for {num_of_items} items is ${total_cost:.2f}")
