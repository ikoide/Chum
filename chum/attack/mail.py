import smtplib, ssl
import csv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from ..util.color import Color

class AttackMail():
  def __init__(self, subject, email, content, server, port, password, targets_file):
    self.subject = subject
    self.email = email
    self.content = content
    self.server = server
    self.port = port
    self.password = password
    self.targets_file = targets_file

  def send_mail(self):
    with open(self.targets_file) as file:
      reader = csv.reader(file)
      next(reader)
      count = 1
      # total = sum(1 for line in open(self.targets_file))
      for name, email in reader:
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.email
        message_text = self.content
        mes = MIMEText(message_text, "html")
        message["To"] = email
        message.attach(mes)

        context = ssl.create_default_context()
        with smtplib.SMTP(self.server, self.port) as server:
          server.ehlo()
          server.starttls(context=context)
          server.ehlo()
          server.login(self.email, self.password)
          server.sendmail(self.email, email, message.as_string())
          Color.p(f"[+] Mail sent to {email} ({count}/{self.file_len(self.targets_file) - 1})")
        count += 1
      Color.p("[*] Attack Complete")

  def file_len(self, fname):
    with open(fname) as f:
      for i, l in enumerate(f):
        pass
    return i + 1

  def run(self):
    self.send_mail()

if __name__ == '__main__':
  mail = AttackMail('t', 'MCJCGRCMWTPAYGCXZXCZ@gmail.com', 't', 'smtp.gmail.com', 587, '7qNXnRt8', 'path_to_csv')
  mail.run()
