# what is list comprehension in python?
- where you create a list from another list
  - list is not limited to an actual python list, list comprehension can be used with all data types, like strings, numbers, etc
- abbreviates syntax greatly

## list comprehension syntax
- extracts each item in a sequence into a new value within the defined array
- new_list = [new_item for item in list] 
  - for each item in list create new_item
- loop through each item and sum by 1
  - new_list = [item + 1 for item in list]
- can be used with ranges:
  - multiplies each number in the range by 2 
  - new_list = [num * 2 for num in range(1,5)]

## conditional list comprehension syntax
- conditionally run the code on the left only if the test on the right passes
  - new_list = [new_item for item in list if test] 
- with an actual condition:
  - short_names = [name for name in names if len(name)< 5]