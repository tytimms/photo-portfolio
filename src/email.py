from flask_mail import Message
from src import mail

def send_message(email, name, message, phone):
  msg = Message(subject='Photo Edit Shop Message', sender=("Photo Edit Shop", mail.MAIL_USERNAME), recipients=['ty.timms16@gmail.com'])
  msg.body = '\nName: ' + name + '\n\nMessage: ' + message + '\n\n Reply to: ' + email + '\n\nPhone Number: ' + phone
  mail.send(msg)
