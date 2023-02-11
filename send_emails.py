from email.message import EmailMessage
from send_emails import password
import ssl
import smtplib
from smtplib import smtp

email_sender = 'ohl68044@gmail.com'
email_password = 'pclrkyivfsqxaskl'

email_receiver = 'mowax14143@chotunai.com'

subject = "Hello there!"
body = """
How are you doing?
"""

em = EmailMessage
em['From'] =  email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content()

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context):
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())