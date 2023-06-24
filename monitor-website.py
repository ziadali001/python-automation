import requests
import smtplib
import os
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


def send_notifications(email_message):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_message}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def monitor_application():
    try:
        response = requests.get('http://ec2-54-165-87-156.compute-1.amazonaws.com:8080/')
        if response.status_code == 200:
            print('application is running successfully ')
        else:
            print('application down')
            msg = f"Application returned {response.status_code}"
            send_notifications(msg)
    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = 'Application not accessible any more'
        send_notifications(msg)


schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()
