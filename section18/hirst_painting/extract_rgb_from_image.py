# extract rgb values from image
## using cologram library https://pypi.org/project/colorgram.py/
import colorgram

def extract_colors():
  colors = colorgram.extract('image.jpg', 12)
  rgb_colors = []

  for color in colors:
    # extract color from rgb dict
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    # build tuple with extracted values
    new_color = (r, g, b)
    rgb_colors.append(new_color)

  print(rgb_colors)

  return rgb_colors
