# handling exceptions in python
## something that could cause an exception
# try:
#   print('hi')
# ## how to handle the exception
# except:
#   print('error')
# ## how to manage if there were no exceptions
# else:
# ## do this no matter what happens (if there is an exception or not)
# finally:

# general error handling with python
try:
  file = open("a_file.txt")
  a_dictionary = {"key": "value"}
  print(a_dictionary["asdfsad"])
# recommended to use more than try/except - except only catches the first error
## can specify which kind of error to catch
except FileNotFoundError:
  ## does something if there was an error
  print("There was an error")
  ## creates a file if it does not exist
  file = open("a_file.txt", 'w')
  file.write("Something")
## can have multiple except statements to catch different kinds of errors
### can assign a value to error message and use within except
except KeyError as error_message:
  print(f"The key {error_message} does not exist.")
# runs when there are no exceptions in the try statement
else:
  content = file.read()
  print(content)
# finally runs regardless of if there are errors in the try block
finally:
  file.close()
  print("File was closed")