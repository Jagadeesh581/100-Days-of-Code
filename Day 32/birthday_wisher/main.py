import smtplib
import random
import pandas
import datetime as dt


MY_EMAIL = "-----------------------"
PASSWORD = "---------------------"

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

birthday_file = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in birthday_file.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter, "r") as letter_file:
        content = letter_file.read()
        final_letter = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{final_letter}"
        )
