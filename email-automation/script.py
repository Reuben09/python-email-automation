import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from time import sleep
from random import randint


SenderAddress = "sharepdf88@gmail.com"
password = "Creuben/09"

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values
sleep(randint(randint(3,15),randint(15,30)))
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
subject = "Invoice31901 was shared with you."
msg = MIMEMultipart()
msg['Subject'] = subject

body = "You have received an invoice from 'Pringle Law Legal Service' Find Attached.For more information Email - wbp@pringlelw.com or Visit www.pringle-law.com"
msg.attach(MIMEText(body,'plain'))

filename='Invoice.html'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()


for email in emails:
    server.sendmail(SenderAddress, email, text)
server.quit()
print("email sent!!!")
