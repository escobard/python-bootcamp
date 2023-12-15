# basic class definition for python
## class naming follows PascalCase -first letter is capitalized for each word
### almost everything else in python follows snake_case
class User:
  # passes to the next line of code
  pass

# class invocation - creates an object (prototype in js)
user_1 = User();
# extends object with attributes
user_1.id = '001'
user_1.username = 'angela'

print(user_1.username)