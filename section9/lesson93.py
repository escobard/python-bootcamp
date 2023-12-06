# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  grade = student_scores[key]
  if grade > 90:
    student_grades[key] = 'Outstanding'
  elif grade > 80:
    student_grades[key] = 'Exceeds Expectations'
  elif grade > 70:
    student_grades[key] = 'Acceptable'
  else:
    student_grades[key] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)