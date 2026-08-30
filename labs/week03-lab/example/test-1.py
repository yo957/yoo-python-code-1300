def celculate_tax(income):
    tax = 0
    income -= 150000
    amount =min(income, 200000)
    tax += amount*0.05
    income -= amount
    amount =min(income, 300000)
    tax += amount*0.10
    income -= amount
    amount =min(income, 400000)
    tax += amount*0.15
    income -= amount
    amount =min(income, 500000)
    tax += amount*0.20
    income -= amount
    amount =min(income, 600000)
    tax += amount*0.25
    income -= amount
    amount =min(income, 700000)
    tax += amount*0.30
    income -= amount
    amount =min(income, 800000)
    tax += amount*0.35
    income -= amount
    return tax
income = float(input("Enter: "))
tax = celculate_tax(income)
after_tax = income - tax
effective_rate = (tax / income) * 100
print("Taxes to be paid",tax)
print("Income after tax:", after_tax)
print("Effective Tax Rate:", effective_rate, "%")        