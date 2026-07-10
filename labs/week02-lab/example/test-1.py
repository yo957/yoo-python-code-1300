print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

circle = float(input("Enter radius: "))
area = 3.14159 * circle ** 2
print("Circle", circle)
print("Area",area)