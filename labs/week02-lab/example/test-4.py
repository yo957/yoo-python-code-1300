# Template 3: Shopping Calculator

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal
subtotal = item_price * quantity

# TODO: Calculate discount amount
discount = subtotal * (discount_percent / 100)

# TODO: Calculate price after discount
price = subtotal - discount

# TODO: Calculate tax amount
tex = price * (tax_percent / 100)

# TODO: Calculate final total
final_total = price + tex

# TODO: Display itemized receipt
print("Subtotal", subtotal)
print("Discount", discount)
print("Price", price)
print("Tex", tex)
print("Final_total", final_total)
