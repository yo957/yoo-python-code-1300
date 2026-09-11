#เครื่องคํานวนค่าไฟฟ้าแบบขั้นบันได
#เขียนโปรแกรมคํานวนค่าไฟไฟฟ้าจากจํานวนหน่วยไฟฟ้าที่ใช้ในเดือนนั้น โดยใช้ฟังก์ชัน calculate_electricity_cost(units)


def calculate_electricity_cost(units):#สร้างฟังก์ชั่นขึ้นมา

    if units > 200:
        bill = 125.0+150.0+350.0+((units - 200)*4.00)+25 #ถ้าเกิน200ใช้สมการนี้
        print("1-50 unit: 125.0 baht")
        print("51-100 unit: 150.0 baht")
        print("101-120 unit: 70.00 baht")
        print(f"200-{units}unit: {(units-200)*4.00}baht")
        print("Service Fee: 25.00 baht")
        print("Total Electricity cost:",bill,"baht")
    elif units > 100:
        bill = (50*2.50)+(50*3.00)+((units - 100)*3.50)+25 #ถ้าเกิน100ใช้สมการนี้
        print("1-50 unit: 125.0 baht")
        print("51-100 unit: 150.0 baht")
        print(f"101-{units}unit: {(units-100)*3.50}baht")
        print("Service Fee: 25.00 baht")
        print("Total Electricity cost:",bill,"baht")

    elif units > 50:
        bill = 125.0+((units - 50)*3.00)+25
        print("1-50 unit: 125.0 baht")
        print(f"51-{units} unit: {(units-50)*3.00}baht")
        print("Service Fee: 25.00 baht")
        print("Total Electricity cost:",bill,"baht")
    elif units > 0:
        bill = units*2.50+25
        print(f"{units} unit: {(units)*2.50} baht")
        print("Service Fee: 25.00 baht")
        print("Total Electricity cost:",bill,"baht")

    else:
        print("Electricity bill")
while(True):
    print("====โปแกรมคํานวนค่าไฟ====")
    print("1. คํานวนค่าไฟ")
    print("2. ออกจากโปรแกรม")
    choice = input("เลือกเมนู: ")
    if choice == "1":
        units = int(input("กรอกจํานวนหน่วยไฟฟ้า:"))
        calculate_electricity_cost(units) #การเรียกใช้ฟังก์ชั่น
    elif choice == "2":
        break
    else:
        print("หากเลือกเมนูอื่น ให้แจ้งว่าไม่ถูกต้อง")    