# Task C1 — Letter Grade

name = input("Enter student name: ")

math = float(input("Enter Math grade: "))
physics = float(input("Enter Physics grade: "))
python_grade = float(input("Enter Python grade: "))

average = (math + physics + python_grade) / 3

if average >= 90:
    letter_grade = "A"
elif average >= 75:
    letter_grade = "B"
elif average >= 60:
    letter_grade = "C"
elif average >= 50:
    letter_grade = "D"
else:
    letter_grade = "F"

scholarship = average >= 90 and math >= 70 and physics >= 70 and python_grade >= 70

print("=" * 30)
print("Student :", name.upper())
print("Math :", math)
print("Physics :", physics)
print("Python :", python_grade)
print("-" * 30)
print("Average :", round(average, 2))
print("Letter grade :", letter_grade)
print("Scholarship :", scholarship)
print("=" * 30)

# Task C2 — Subject Feedback

grades = [math, physics, python_grade]
subjects = ["Math", "Physics", "Python"]

for i in range(len(grades)):
    if grades[i] >= 90:
        comment = "Excellent"
    elif grades[i] >= 75:
        comment = "Good"
    elif grades[i] >= 60:
        comment = "Satisfactory"
    else:
        comment = "Fail"

    print(subjects[i], ":", grades[i], "→", comment)

# Task C3 — Name Analysis

print("Name uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))
print("Masked name :", name.replace(name[0], "*", 1))