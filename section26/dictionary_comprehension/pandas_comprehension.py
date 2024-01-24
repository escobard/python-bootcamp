import pandas

student_dict = {
  "student": ['Angela', 'James', 'Lily'],
  "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# using comprehension with dataframes
## .row property returns a pandas series
for (index, row) in student_data_frame.iterrows():
  ## can access the value of each row by its key
  print(row.student)
  print(row.score)