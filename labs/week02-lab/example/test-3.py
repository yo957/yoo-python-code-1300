print("3. Compound Interest Calculator:")
print("   - Ask for principal, rate, and time")
print("   - Calculate: A = P * (1 + r/100) ** t")
print()

second = int(input("Insert second : "))
hour = second // 3600
second_remain = second % 3600
minute = second_remain // 60
second_remain = second % 60
print(second ,"second =",hour,"hour, ",minute, "minute, ",second_remain, "second45")