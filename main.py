student_name = input("Enter student name: ")
math_grade = float(input("Enter Math grade: "))
physics_grade = float(input("Enter Physics grade: "))
python_grade = float(input("Enter Python grade: "))

average = (math_grade + physics_grade + python_grade) / 3
scholarship = 35000 if average >= 90 else 0
gpa = average / 25

print("=" * 30)
print("STUDENT REPORT CARD")
print("=" * 30)
print("Student :", student_name)
print("Math :", math_grade)
print("Physics :", physics_grade)
print("Python :", python_grade)
print("-" * 30)
print("Average :", round(average, 2))
print("GPA :", round(gpa, 2))
print("Scholarship :", scholarship, "KZT")
print("=" * 30)

print("Scholarship granted:", average >= 90)
print("Perfect score:", math_grade == 100 and physics_grade == 100 and python_grade == 100)