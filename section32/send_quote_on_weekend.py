
# challenge - send a motivational quote to the target email address every week on Tuesday

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day_of_week = now.weekday()

email = "escobardtraining@gmail.com"
password = "tpsx mkhh gfpp zxnf"

email_to = "escobardautomation@yahoo.com"

## check if day of the week is sunday, and send email if it is
if day_of_week == 6:

  ## open file and store contents as list
  with open("quotes.txt") as quotes_file:
    file_data = quotes_file.readlines()
    # pick a random quote
    random_quote = random.choice(file_data)
    print(random_quote)

  ## send email quote
  with smtplib.SMTP("smtp.gmail.com", port=587) as gmail_connection:
    gmail_connection.starttls()
    gmail_connection.login(user=email, password=password)
    gmail_connection.sendmail(
      from_addr=email,
      to_addrs=email_to,
      msg=f"Subject:Sunday motivation\n\n{random_quote}")