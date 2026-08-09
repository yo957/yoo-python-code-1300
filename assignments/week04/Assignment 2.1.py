scores = []#รอรับข้อมูลเข้าเหมือนกล่องให้litsที่จะเข้าเก็บ

for i in range(1, 6):
    score = float(input(f"Enter score for student {i}: "))
    scores.append(score)

print("\n--- Examination Results ---")

for i, score in enumerate(scores, start=1):
    if score >= 50:
        result = "Passed"
    else:
        result = "Failed"
    
    print(f"Student {i} (Score: {score}): {result}")