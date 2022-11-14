import smtplib
import random
import datetime as dt


MY_EMAIL = "_____________@gmail.com"
PASSWORD = "-------------"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\nHi Jagadeesh,\n{quote}"
        )


# # ------------------------------- Sending email using smtplib ---------------------------------------
# import smtplib
#
# my_email = "__________@yahoo.com"
# password = "__________"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="_____________@gmail.com",
#         msg="Subject:Hello\n\nThis body part of the mail.",
#     )

# # ---------------------------------- Using datetime Module ---------------------------------------------
# import datetime as dt
#
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year=2000, month=6, day=19)
# print(date_of_birth)
