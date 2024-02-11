import smtplib

email = "escobardautomation@gmail.com"
# google does not allow you to use the password rquired to login, must instead use a 2fa password
## https://support.google.com/accounts/answer/185833?hl=en
password = "hmtv yifz sazc dbgo"

email_to = "escobardautomation@yahoo.com"

# creates a connection to email provider
## every email provider has a different SMTP address
gmail_connection = smtplib.SMTP("smtp.gmail.com", port=587)
# establishes connection with provider
gmail_connection.starttls()
gmail_connection.login(user=email, password=password)
# email without a subject is likely to be flagged as spam!
gmail_connection.sendmail(from_addr=email, to_addrs=email_to, msg="Subject:Hello\n\nThis is the body of the email")
# closes the connection to smtp client
gmail_connection.close()

# can avoid the .close() method by using the with loop to connect to smtp
## eg, with smtplib.smtp() as gmail_connection:
