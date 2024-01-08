import pandas

# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw


data = pandas.read_csv('squirrel_data.csv')

fur_color_gray = len(data[data['Primary Fur Color'] == 'Gray'])
fur_color_cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
fur_color_black = len(data[data['Primary Fur Color'] == 'Black'])

fur_count = {
  'Fur Color': ['Gray', 'Cinnamon', 'Black'],
  'Count': [fur_color_gray, fur_color_cinnamon, fur_color_black]
}

dataframe = pandas.DataFrame(fur_count)

# convert existing or new data frames to csv
dataframe.to_csv('new_data_squirrels.csv')