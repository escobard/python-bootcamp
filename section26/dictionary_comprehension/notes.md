# dictionary comprehension
- similar to list comprehension, syntax sugar to convert a dictionary from a data structure (any sequential data type!)
- sample syntax:
  - new dict = {new_key:new_value for item in list}
- loop through each item in a dictionary and split into key,value, append key,value to new dictionary
  - new dict = {new_key:new_value for (key,value) in dict.items()}