# without libraries, this is the recommended approach to read csv data
## still much simpler than with JS, awesome!
# with open('weather_data.csv') as weather_data:
#   weather_list = weather_data.readlines()
#   print(weather_list)

# python's inbuilt csv reading and writing library
import csv

# lots of convoluted syntax to read data, libraries would help shorten the syntax below
## still, syntax is much simpler out of the box than the same with JS, love python!
with open("weather_data.csv") as data_file:
  data = csv.reader(data_file)
  temperatures = []
  for row in data:
    if row[1] != 'temp':
      temperatures.append(int(row[1]))
      print(row)

  print(temperatures)