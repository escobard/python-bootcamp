# functions with outputs

def format_name(f_name, l_name):
  # title helper function makes the first letter of every string word a capital
  return f_name.title() + " " + l_name.title()

result = format_name('Dan', 'ESCObar')

print(result)