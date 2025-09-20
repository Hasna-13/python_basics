students = {"Alice": 85, "Bob": 92, "Charlie": 78}

print("Grade Tracker")
print("Students:", students)

average = sum(students.values()) / len(students)
print("Average grade:", average)


highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print(f"Highest scorer: {highest} ({students[highest]})")
print(f"Lowest scorer: {lowest} ({students[lowest]})")

students["David"] = 88
students["Alice"] = 90
print("Updated Students:", students)
