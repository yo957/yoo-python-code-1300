#รับข้อมูล "ชื่อจริง (เป็นภาษาอังกฤษ)" จากผู้ใช้
#นับจํานวนสระในข้อความดังกล่าว

#ตัวอย่างหน้าจอ
#What is your name ? : Nitis
#You have 4 vowels in your text.

name = input("Enter your name eng? :")
name = "Nitis"
letters = list(name)
print(letters)
caunter = 0

for char in letters:
    if char == 'a' or char == 'A':
        caunter = caunter +1
    elif char == 'e' or char == 'E':
            caunter = caunter +1
    elif char == 'i' or char == 'I':
            caunter = caunter +1
    elif char == 'o' or char == 'O':
            caunter = caunter +1
    elif char == 'u' or char == 'U':
            caunter = caunter +1
print("You have", caunter, "vawels in your text.")