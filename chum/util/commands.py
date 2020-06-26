import csv
import os

from ..util.color import Color
from ..util.countdown import countdown
from ..attack.mail import AttackMail
from ..config import Configuration

class Command():
  @staticmethod
  def help():
    Color.p("\n--- {C}Help Page{W} ---")
    Color.p("attack")
    Color.p("banner")
    Color.p("quit")
    # Color.p("l_targets\n")
    Color.p("Enter 'help command' to learn more.\n")

  @staticmethod
  def banner():
    Color.p("\n{C}          /`·.¸")
    Color.p("         /¸...¸`:·")
    Color.p("    ¸.·´  {D}¸{W}{C}   `·.¸.·´)  {C}Chum {D}%s{W}" % Configuration.version)
    Color.p("{C}   : {R}©{C} {D}):´;{W}{C}      ¸  {   {W}{D}Created: 05/20/20{W}")
    Color.p("{C}    `·.¸ {D}`·{W}{C}  ¸.·´\`·¸)  {G}Author: Ian Koide")
    Color.p("{C}         `\\\´´\¸.·´{W}\n")

  @staticmethod
  def quit():
    pass

  @staticmethod
  def attack():
    Color.p("\n--- {C}Attack{W} ---")
    try:
      with open(os.getcwd() + "/chum/config.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for server, port, subject, content, email, password, targets_file in reader:
          server = server
          port = port
          subject = subject
          content = content
          email = email
          password = password
          targets_file = os.getcwd() + "/targets/" + targets_file
        Color.p("[*] Config file found.")
      Color.p("[?] Would you like to use this config file? [Y/N]")
      userIp = input("-[ ")
      if userIp == "y" or userIp == "Y":
        Color.p("[*] Config loaded successfully.")
      elif userIp == "n" or userIp == "N":
        server = input("-[ Server: ")
        port = input("-[ Port (default - 578): ")
        subject = input("-[ Subject: ")
        content = input("-[ Content: ")
        email = input("-[ Email: ")
        password = input("-[ Password: ")
        targets_file = input("-[ Targets File (default - targets.csv): ")
      else:
        Color.p("[!] Please enter either a Y or N.")
    except:
      Color.p("[!] No config file found or config loaded unsuccessfully. Requesting details now.")
      server = input("-[ Server: ")
      port = input("-[ Port (default - 578): ")
      subject = input("-[ Subject: ")
      content = input("-[ Content: ")
      email = input("-[ Email: ")
      password = input("-[ Password: ")
      targets_file = input("-[ Targets File (default - targets.csv): ")

    Color.p("[*] Please press enter to launch attack.")
    launch = input("")
    Color.p("{R}Attack launching in 15 seconds. CTRL C to cancel.{W}")
    countdown(int(15))
    mail = AttackMail(subject, email, content, server, port, password, targets_file)
    mail.run()