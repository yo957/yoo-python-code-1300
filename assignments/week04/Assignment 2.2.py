prices = []#รอรับข้อมูลเข้าเหมือนกล่องให้litsที่จะเข้าเก็บ6ตัวตามfor
print("Enter prices of 6 items:")
for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    prices.append(price)

budget = int(input("\nEnter total budget: "))#งบที่มี
print()

total_spent = 0
bought_items = []

for i, price in enumerate(prices, start=1):
    if total_spent + price <= budget:
        print(f"Item {i} = {price} -> buy")
        total_spent += price
        bought_items.append(price)
    else:
        print(f"Item {i} = {price} -> cannot buy")
    
    print(f"Current total = {total_spent}\n")

print(f"Bought items: {bought_items}")
print(f"Total spent: {total_spent}")
print(f"Remaining budget: {budget - total_spent}")