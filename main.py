import smtplib
import random
import datetime as dt


def send_email():
    quote = random.choice(quote_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Makes connection secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivational Quote of the Day!\n\n{quote}")


my_email = "my_email"
password = "my_password"

with open("quotes.txt") as file:
    quote_list = file.readlines()

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 0:
    send_email()
