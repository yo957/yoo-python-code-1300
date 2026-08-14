'''''
print("=== PART 1: BASIC FUNCTIONS ===")

# Example 1: Simple function without parameters(คือข้อมูลย่อยของฟังชั่นคนอยากใช้ใช้ได้เลยไม่ต้องสั่งฟังชั่น)
def say_hello():
    """A simple function that prints a greeting"""
    print("Hello, World!")
    print("Welcome to Python functions!")

# Calling the function
print("Calling say_hello():")
say_hello()
print()
'''''
'''''
def introduce_person(name, age, city):#ตัวอย่างcodeของการใช้ฟังชั่น3ตัว
    """Introduces a person with their details"""
    print(f"Hi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")
    print()

print("Calling introduce_person:")
introduce_person("Diana", 25, "New York")
introduce_person("Eve", 30, "Los Angeles")
'''''
'''''
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)#บรรทัด68ถึง69เป็นการเรียกใช้ตั้งแต่ชื่อผู้และวนกลับเข้าฟังชั่นจนจบ
calculate_rectangle_area(10, 7)
'''''
'''''
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()
'''''
'''''
def get_circle_info(radius):#ตัวอย่างการเขียนโปรแกรมค่ากลับแต่2เรื่อง
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    volumn = 4.0 / 3 * pi * radius**3
    return area, circumference, volumn

print("Circle calculations:")#แต่บรรทัดนี้ถึงบรรทัด104คือตัวแปลนอกฟังชั่น
radius = 5
area, circumference, volumn = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()
'''''
'''''
def greet_with_title(name, title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prot.")  # Custom title
print()
'''''
'''''
def power(base, exponent=2):
    """Calculates base raised to exponent (default: square)"""
    return base ** exponent

print("Power function with defaults:")
print(f"power(5) = {power(5)}")  # Square
print(f"power(5, 3) = {power(5, 3)}")  # Cube
print(f"power(2, 4) = {power(2, 4)}")  # Fourth power
print()
'''''
"""
เขียน function ชื่อ convert_currency()
ที่ทําหน้าที่ในการแปลงสกุล
THB <-> USD

ตัวอย่างหน้าจอ
100THB =3.33 USD
100USD =3300.0 THB
"""

def couvert_currency(value, currency):
    if currency == "USD":
        result = value / 33
        print(f"{value}THB +{result:.2f}USD")
    elif currency == "THB":
        result = value * 33
        print(f"{value}USD +{result:.2f}THB")

couvert_currency(100,"USD")
couvert_currency(100,"THB")
