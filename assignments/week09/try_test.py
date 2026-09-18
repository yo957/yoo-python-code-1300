try:
    a = float(input("กรอกตัวเลขที่1: "))
    b = float(input("กรอกตัวเลขที่2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")
    result = 0
    if operator =="+":
        result = a+b
    elif operator =="-":
        result = a-b
    elif operator =="*":
        result = a*b
    elif operator =="/":
        result = a/b
    else:
        raise ValueError("เครื่องหมายต้องเป็น + - * / เท่านั้น")
    print(f"{a} {operator} {b} = {result}")
except ValueError:
    print("กรุณากรอกตัวเลขให้ถูกต้อง")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

else:
    print("ทํางานได้สมบูรณ์")

finally:
    print("จบการทํางาน")