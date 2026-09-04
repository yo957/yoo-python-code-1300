"""""
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert the text :")
char = input("Insert the cher :")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")
"""""
password = input("Insert your password : ")
if len (password) >=8:
    print("You password is not strong!")
else:
    print("You password is strong")
print(f"islower(): {password.isalnum()}")
    