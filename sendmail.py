
# Import modules
import smtplib
from email.message import EmailMessage

# content
sender = "samuelsampene@hotmail.com"
reciever = "samuelsampene@yahoo.com"
password = "Vision2020"
msg_body = 'Email sent using outlook!'

# action
msg = EmailMessage()
msg['subject'] = 'Email sent using outlook.'
msg['from'] = sender
msg['to'] = reciever
msg.set_content(msg_body)

with smtplib.SMTP_SSL('smtp-mail.outlook.com', 465) as smtp:
    smtp.login(sender,password)
    smtp.send_message(msg)
    smtp.quit()
