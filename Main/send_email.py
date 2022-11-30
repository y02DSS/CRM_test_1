from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
 

from django.db.models.fields.files import FileDescriptor

def send_for_email(email, text, date, organization, file=None):
    msg = MIMEMultipart()
    password = "epvqrunyrfhcwihf"
    msg['From'] = "testserversergei@gmail.com"
    msg['To'] = email
    msg['Subject'] = f'{date} {organization}'

    msg.attach(MIMEText(text))

    if file is not None:
        attachment = MIMEBase('application', "octet-stream")
        attachment.set_payload(open(file.path, "rb").read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=file.name.split('/')[-1])
        msg.attach(attachment)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    # server.ehlo()
    server.login(msg['From'], password)
    server.send_message(msg)
    server.quit()
    
