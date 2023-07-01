import smtplib

my_email = "your.email@gmail.com"
my_pass = "your_password" # in gmail generated password for app (see https://support.google.com/mail/?p=InvalidSecondFactor)

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=my_pass)
connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Hello\n\nThis is the body of my email.")
print(f"Mail sent to {my_email}.")
connection.close()