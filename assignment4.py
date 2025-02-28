# Students Grade System
student_name = input("Enter student name: ")
student_grade = int(input("Enter student grade: "))
student_age = int(input("Enter student age: "))
# If-else statement
if student_grade >= 90:
    print("Student grade is A")
else:
    print("Student grade is not A")
# If-elif-else statement
if student_grade >= 90:
    print("Student grade is A")
elif student_grade >= 80:
    print("Student grade is B")
else:
    print("Student grade is not A or B")
# Nested if-else statement
if student_grade >= 90:
    if student_age >= 18:
        print("Student is an adult with grade A")
    else:
        print("Student is a minor with grade A")
else:
    print("Student grade is not A")
# Multiple if statement
if student_grade >= 90 and student_age >= 18:
    print("Student is an adult with grade A")
if student_grade >= 80 and student_age < 18:
    print("Student is a minor with grade B")
# If-else statement with multiple conditions
if student_grade >= 90 and student_age >= 18 and student_name == "Ram":
    print("Ram is an adult with grade A")
else:
    print("Student is not Ram or not an adult with grade A")
# Elif statement with multiple conditions
if student_grade >= 90:
    print("Student grade is A")
elif student_grade >= 80 and student_age >= 18:
    print("Student is an adult with grade B")
else:
    print("Student grade is not A or B")
# Using if statement with 'in' operator
grades = [90, 80, 70, 60, 50]
if student_grade in grades:
    print("Student grade is valid")
else:
    print("Student grade is not valid")
# Using if statement with arithmetic operators
if student_grade > 90 - 10:
    print("Student grade is above 80")
else:
    print("Student grade is below 80")
# Using if statement with comparison operators
if student_grade == 90:
 print("Student grade is exactly 90")
else:
    print("Student grade is not exactly 90")
# Using if statement with logical operators
if student_grade >= 90 and student_age >= 18 or student_name == "Ram":
    print("Student meets the criteria")
else:
    print("Student does not meet the criteria")
