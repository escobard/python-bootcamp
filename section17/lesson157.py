class User:
  def __init__(self, user, username):
    print('New user is being created')
    self.user = user
    self.username = username
    self.followers = 0
    self.following = 0

  # base method definition with python classes
  ## self argument is required for each class method
  def follow(self, user):
    user.followers += 1
    self.following += 1

user_1 = User(1, 'Dan')
user_2 = User(2, 'Angela')

# invoke class method in python
user_1.follow(user_2)
print(user_1.username, 'is following', user_1.following, 'user')
print(user_2.username, 'has ', user_2.followers, ' followers')
