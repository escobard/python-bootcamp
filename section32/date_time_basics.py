import datetime as dt

## prints current date and time
now = dt.datetime.now()
## can select specific parts of the date to make date easier to parse and manipulate programatically
year = now.min
## gives you a day of the week
day_of_week = now.weekday()

## can create a date with specific values - like with js new Date
date_of_birth = dt.datetime(year=1990, month=8, day=22)
print(date_of_birth)