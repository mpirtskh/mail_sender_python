import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import sys


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Mariam Phirtskhalava'
email['to'] = ['phirtskhalavamariam@gmail.com', 'levankhelo@gmail.com' ,'luka.todua@gtu.ge', 'nxslasher@gmail.com']
email['subject'] = "Mail From Python Script!!!"

email.set_content(html.substitute(person_name="Joahn"), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mgp1998.13@gmail.com','Qwerty89000123')
    smtp.send_message(email)
    print('All DOne!')