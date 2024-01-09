# great library to manage 2 dimensional data
## https://pandas.pydata.org/docs/index.html
import pandas

data = pandas.read_csv('weather_data.csv')

# very nicely formatted data in a table format
# print(data)

# shorthand in pandas to grab all data from specified column

# can use the type method to check the type of data
## <class 'pandas.core.frame.DataFrame'> - a pandas class object, wrapper around fetched data
### every single column is considered a series, which is a list of single column
#### more on different data structures suppored by pandas - https://pandas.pydata.org/docs/user_guide/dsintro.html
# print(type(data))

# creates fetched data and turns it into a python dictionary
## python dictionaries are very similar to JSON - https://www.w3schools.com/python/python_dictionaries.asp
# data_dict = data.to_dict()
# print(data_dict)

# converts a specific series (or column data set) into a python list
## more on conversions with panda's series
series_list = data["temp"].to_list()

# challenge- calculate average temp
# average_temp = sum(series_list) / len(series_list)
# print(average_temp)
# using pandas, we can find the average of a series with
# print(data["temp"].mean())

# find the max value in a series
# print(data["temp"].max())


# can fetch data by column using pandas array shorthand (case sensitive)
# print(data['temp'])
# can also fetch data by colum using pandas dictionary shorthand (case sensitive) b
# print(data.temp)

# can fetch data row with conditions - AMAZING
monday = data[data.day == 'Monday']
print(monday)

## more complicated conditional row fetching
## print(data[data.temp == data.temp.max()])

# can use result from row conditional fetches to further filter data
print(monday.condition)

# create dataframe from scratch
data_dict = {
  "students": ['Jon', 'Betty', 'Ben']
}

dataframe = pandas.DataFrame(data_dict)

# convert existing or new data frames to csv
dataframe.to_csv('new_data.csv')