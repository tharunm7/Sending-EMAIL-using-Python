import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.mailtrap.io', 2525)
server.ehlo()

with open('credentials.txt', 'r') as p:
    password = p.read()

server.login('youremail@gmail.com', 'password')

msg = MIMEMultipart()
msg['From'] = 'Your Name'
msg['To'] = 'receiptentemail@gmail.com'
msg['Subject'] = 'JUST A TEST EMAIL'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'img.jpg'
attachement = open(filename, 'rb')                                              

payload = MIMEBase('application','octet-stream')                                
payload.set_payload(attachement.read())

encoders.encode_base64(payload)                                                 
payload.add_header('Content-Disposition', f'attachment;filename={filename}')
msg.attach(payload)
text = msg.as_string()
server.sendmail('youremail@gmail.com', 'receiptentemail@gmail.com', text)