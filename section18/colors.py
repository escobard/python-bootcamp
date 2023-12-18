import random

colors = ['GreenYellow', 'Chocolate', 'Gold', 'LightSeaGreen', 'SkyBlue', 'MediumBlue', 'DodgerBlue', 'Brown', 'LightSkyBlue']

## generate random RGB color
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  # return a tuple with the color selection
  return (r, g, b)