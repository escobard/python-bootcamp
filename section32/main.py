import random
# challenge - send a motivational quote to the target email address every week on Tuesday

## open file and store contents as list
with open("quotes.txt") as quotes_file:
  file_data = quotes_file.readlines()
  # pick a random quote
  random_quote = random.choices(file_data)
  print(random_quote)

## send email quote
import smtplib

email = "escobardtraining@gmail.com"
password = "tpsx mkhh gfpp zxnf"

email_to = "escobardautomation@yahoo.com"

gmail_connection = smtplib.SMTP("smtp.gmail.com", port=587)

gmail_connection.starttls()
gmail_connection.login(user=email, password=password)
gmail_connection.sendmail(from_addr=email, to_addrs=email_to, msg=f"Subject:Weekly quote\n\n{random_quote[0]}")
gmail_connection.close()