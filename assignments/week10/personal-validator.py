"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
print("=== PERSONAL INFORMATION VALIDATOR ===")
Name = input("Enter your name: ")
Age = input("Enter your age: ")
PhoneNumber = input("Enter your phone number: ")

print("Validation Results: ")
for char in Name:
    if char.isalpha() or char.isspace():
        check_name = True
    else:
        check_name = False
        break
check_age = False
if Age >= 18 and Age <= 65:
    check_age = True

check_Name = False
if Name.isdigit():
    check_Name = True

check_phone = False
if PhoneNumber.isdigit() and len(PhoneNumber) == 10:
    check_PhoneNumber = True
else:
    print("Name: Invalid")

if check_age:
    print(f"Age: Valid ({Age} years old)")
else:
    print("Age: Invalid")

if check_PhoneNumber:
    print("Phone: valid(10-digit number)")
else:
    print("PhoneNumber: Invalid")

print("Formatted Information: ")
print(f"Name: {Name.upper()}")
if 18 <= Age <=30:
    print("Age Group: Voung Aduit (10-30)")
else 31 <= Age <= 60:
    print("Age Group: Voung Aduit (31-60)")
else:
    print("Age Group: senior")
    print(f"Phone: +91-{PhoneNumber}")