# class with constructors
class User:
  # base class init (constructor) definition
  ## this function gets triggered every time the class is initialized
  def __init__(self, user, username):
    print('New user is being created')
    ## assigns a constructor argument into the class object on initiation
    self.user = user
    self.username = username
    ## can set a default value without arguments
    self.followers = 0


user_1 = User(1, 'Dan')
print('User attributes: ', 'User: ', user_1.user, 'Username: ', user_1.username, 'Followers: : ', user_1.followers)
