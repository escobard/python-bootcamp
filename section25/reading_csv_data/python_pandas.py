# great library to manage 2 dimensional data
## https://pandas.pydata.org/docs/index.html
import pandas

data = pandas.read_csv('weather_data.csv')
print(data)
# shorthand in pandas to grab all data from specified column
print(data['temp'])