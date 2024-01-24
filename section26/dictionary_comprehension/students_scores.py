## data filtering with dictionary comprehension
names = ['Al', 'Phonse', 'Ed', 'Mustang', 'Father']
import random
students_scores = {name:random.randint(1,100) for name in names}
students_scores = {name:random.randint(1,100) for name in names}
passed_students = {key:value for (key,value) in students_scores.items() if value > 50}