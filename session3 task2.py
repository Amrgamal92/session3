# 1. Create a list of dictionaries
students = [
    {"name": "Ali", "grades": [80, 90, 88]},
    {"name": "omar", "grades": [90, 75, 80]},
    {"name": "Amr", "grades": [60, 88, 95]}
]

# 2. Script to calculate and print average grades
for student in students:
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"{student['name']}: Average Grade = {average:.2f}")
