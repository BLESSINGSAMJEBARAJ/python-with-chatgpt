marks = [int(input(f"Enter mark {i+1}: ")) for i in range(5)]
average = sum(marks) / len(marks)

print("\nTotal:", sum(marks))
print("Average:", round(average, 2))

if average >= 90: grade = "A+"
elif average >= 80: grade = "A"
elif average >= 70: grade = "B"
elif average >= 60: grade = "C"
elif average >= 50: grade = "D"
else: grade = "FAIL"

print("Grade:", grade)
