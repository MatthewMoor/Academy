import os
from sendgrid import SendGridAPIClient
from django.conf import settings
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email=settings.EMAIL_HOST_USER,
    to_emails='meccep.98.98@mail.ru',
    subject='Sending with Django SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(settings.SEND_GRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)