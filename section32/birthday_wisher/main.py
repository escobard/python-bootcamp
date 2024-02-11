##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# # instructor solution
# from datetime import datetime
# import pandas
#
# today = datetime.now
#
# ## build tupple to store today's date
# today_tuple = (datetime.now().month, datetime.now().day)
#
# ## import csv data with pandas
# data = pandas.read_csv("birthdays.csv")
#
# ## creates a new dictionary where each row has its own key
# ### using pandas' data.iterrows() returns each row as its own dict
# birthdays_dict = {
#   ## creates a tuple key - that's new
#   (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
# }

# my solution
import pandas
import datetime as dt
import random
import smtplib

email = "escobardtraining@gmail.com"
password = "tpsx mkhh gfpp zxnf"

email_to = "escobardautomation@yahoo.com"

## extract birthday data from csv
birthday_data = pandas.read_csv("birthdays.csv")
birthday_data_rows = birthday_data.iterrows()
# print(birthday_data_rows)

birthday_list = birthday_data.to_dict()

## set today's date to check birthday data
today = dt.datetime.now()

for (index, data_row) in birthday_data_rows:

  if today.year == data_row.year and today.month == data_row.month and today.day == data_row.day:

    ## pick a random letter from the letter template
    letters = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
    random_letter = random.choice(letters)

    ## replace the [NAME] with the person's actual name
    with open(random_letter) as letter:
      ### using data_row["name"] instead of data_row.name - key value is returning incorrect value
      data = letter.read().replace("[NAME]", data_row["name"])

      ## send the letter generated to that person's email address
      with smtplib.SMTP("smtp.gmail.com", port=587) as gmail_connection:
        gmail_connection.starttls()
        gmail_connection.login(user=email, password=password)
        gmail_connection.sendmail(
          from_addr=email,
          to_addrs=data_row.email,
          msg=f"Subject:Happy birthday!\n\n{data}")

