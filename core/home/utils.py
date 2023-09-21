from home.models import Student
import time
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def runthis_func():
    print("Function Started")
    time.sleep(1)
    print("Function Ended")


def send_email_to_client():
    subject="This email is from Django server and is for testing purpose only."
    message="This is a test Message from Sachin."
    from_email=settings.EMAIL_HOST_USER
    recipient_list=['temporaryzdkjfglkdfbg@gmail.com']
    send_mail(subject,message,from_email,recipient_list)

def send_email_with_attachment(subject,message,recipient_list,file_path):
    mail=EmailMessage(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER,to=recipient_list)
    mail.attach_file(file_path)
    mail.send()
