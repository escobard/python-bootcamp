# You are going to write a program that calculates the average student height from a List of heights.
# [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

print("input a Python list of student heights seperated by spaces, eg - 151 145 179")
student_heights = input().split()
students = len(student_heights)
for n in range(0, students):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
for student_height in student_heights:
  total_height += student_height
  ## without arguments, round() rounds the number up to the nearest whole number
average_height = round(total_height / students)
print(f'total height = {total_height}')
print(f'number of students = {students}')
print(f'average height = {average_height}')