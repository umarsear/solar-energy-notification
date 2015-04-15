__author__ = 'umasear'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser
import sys

parser = ConfigParser()

if len(sys.argv) > 1:
    parser.read(sys.argv[1])
else:
    parser.read('solar_notification.ini')

from_email = parser.get('mail_server','email_address')
server_address = parser.get('mail_server','server_address')
server_port = parser.get('mail_server','server_port')
server_protocol = parser.get('mail_server','server_protocol')
server_username = parser.get('mail_server','username')
server_password = parser.get('mail_server','password')

text = "Hi {},\n\nYour solar system produced {} KWhr of energy today\n\nThe solar notification service"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi {},<br><br>
       Your solar system produced <b>{} KWhr</b> of energy today<br><br>
       Notification service provided by <a href="http://www.infinitypower.solar">Infinity Power Solutions</a> .
    </p>
  </body>
</html>
"""


def send_email(owner, email_to, subject, power):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = email_to
    part1 = MIMEText(text.format(owner,power), 'plain')
    part2 = MIMEText(html.format(owner,power), 'html')
    msg.attach(part1)
    msg.attach(part2)
    username = server_username
    password = server_password
    server = smtplib.SMTP('{}:{}'.format(server_address,server_port))
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email, email_to, msg.as_string())
    server.quit()