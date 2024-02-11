##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import smtplib

email = "escobardtraining@gmail.com"
password = "tpsx mkhh gfpp zxnf"

email_to = "escobardautomation@yahoo.com"

## extract birthday data from csv
birthday_data = pandas.read_csv("birthdays.csv")

birthday_list = birthday_data.to_dict()

## set today's date to check birthday data
today = dt.datetime.now()

if today.year in birthday_list["year"].values() and today.month in birthday_list["month"].values() and today.day in birthday_list["day"].values():
  print('True!')

  ## pick a random letter from the letter template
  letters = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
  random_letter = random.choice(letters)

  ## replace the [NAME] with the person's actual name
  with open(random_letter) as letter:
    data = letter.read().replace("[NAME]", "Name")

    ## send the letter generated to that person's email address
    with smtplib.SMTP("smtp.gmail.com", port=587) as gmail_connection:
      gmail_connection.starttls()
      gmail_connection.login(user=email, password=password)
      gmail_connection.sendmail(
        from_addr=email,
        to_addrs=email_to,
        msg=f"Subject:Happy birthday!\n\n{data}")

