# open a file from any location
## file = open('my_file.txt')
# forces python to close the file
##file.close()


# open a file using python with, creating a loop of sorts until all operations in the file are complete
# closes the file without having to specify file.close()
with open('my_file.txt') as file:
  # reads the content of the file and stores to contents variable
  contents = file.read()
  # prints the content to the console!
  print(contents)

# writes to file
## mode w to write, which overwrites existing content
### can create a new file using write mode, then write to the file
with open('new_file.txt', mode='w') as file:
  file.write('New text')

## mode a to append, which appends to existing content
# with open('my_file.txt', mode='a') as file:
#    file.write('\nNew text')