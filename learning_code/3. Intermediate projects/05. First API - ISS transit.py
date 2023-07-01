import requests
import smtplib
from datetime import datetime, timedelta

MY_LAT = 48.091331
MY_LONG = 17.065950

response = requests.get(url="http://api.open-notify.org/iss-now.json")
#print(response.json()['iss_position'])

iss_longitude = float(response.json()['iss_position']['longitude'])
iss_latitude = float(response.json()['iss_position']['latitude'])

iss_position = (iss_longitude, iss_latitude)
print(f"ISS position right now is: lat: {iss_latitude}, long: {iss_longitude}.")

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
}

daytime_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
daytime_response.raise_for_status
sunrise = daytime_response.json()["results"]["sunrise"]
sunset = daytime_response.json()["results"]["sunset"]

visible_from = daytime_response.json()["results"]["civil_twilight_end"].split("T")[1].split("+")[0]
print(f"The Civil twilight starts at {visible_from} (+2h for SELC).")
degrees_under = iss_latitude - 27

if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
    print(f"ISS is near zenith!")
    my_email = "roman.vanur@gmail.com"
    my_pass = "tlqpntwlkjggwydq" # in gmail generated password for app (see https://support.google.com/mail/?p=InvalidSecondFactor)
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:ISS is visible!\n\nThis is the body of my email.")
    #print(f"Mail sent to {my_email}.")
    connection.close()

else:
    print(f"ISS is not visible. Diff lat = {MY_LAT - iss_latitude}, Diff long = {MY_LONG - iss_longitude}.")


# check if its day or night at that time - check with nautical_twilight_begin
