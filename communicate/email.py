
import logging
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send(to=None, process=None, subject_format='{executable} process {pid} ended'):
    """Send email about the ended process.

    :param to: email addresses to send to
    :param process: information about process. (.info() inserted into body)
    :param subject_format: subject format string. (uses process.__dict__)
    """
    if to is None:
        raise ValueError('to keyword arg required')

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "thibault.ribayrol@gmail.com"
    receiver_email = to
    password = "L8btoswwacorte"

    msg = MIMEMultipart("alternative")
    msg['From'] = "Beamler <{}>".format(sender_email)
    msg['To'] = ', '.join(to)
    msg['Subject'] = "Beamler's Server is DOWN"
    body = """\
    Hi there, 

    admin.beamler.com is probably down, you have to restart it.
    
    """ + process.info() + """\
    

    This message is sent from Python."""
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls()
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()




    
    