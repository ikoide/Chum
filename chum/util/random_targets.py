import os
import string
import random

def random_emails(amount, length):
  emails = []
  for i in range(amount):
    letters = string.ascii_lowercase
    emails.append(''.join(random.choice(letters) for i in range(length)) + "@gmail.com")
  return emails

random_emails = random_emails(100, 10)
for i in random_emails:
  print("First Last," + i)