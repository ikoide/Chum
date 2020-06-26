import os
import sys

from .config import Configuration
from .util.color import Color
from .util.commands import Command

class Chum():
  def __init__(self):
    self.running = True
    self.print_banner()

  def print_banner(self):
    Color.p("\n{C}          /`·.¸")
    Color.p("         /¸...¸`:·")
    Color.p("    ¸.·´  {D}¸{W}{C}   `·.¸.·´)  {C}Chum {D}%s{W}" % Configuration.version)
    Color.p("{C}   : {R}©{C} {D}):´;{W}{C}      ¸  {   {W}{D}Created: 05/20/20{W}")
    Color.p("{C}    `·.¸ {D}`·{W}{C}  ¸.·´\`·¸)  {G}Author: ?")
    Color.p("{C}         `\\\´´\¸.·´{W}\n")

  def start(self):
    while self.running:
      userIp = input("-[ ")
      if userIp == 'quit':
        self.running = False
        sys.exit()
      try:
        result = getattr(Command, userIp)()
      except AttributeError:
        Color.p("[!] Not valid command.")
  
def entry_point():
  try:
    chum = Chum()
    chum.start()
  except Exception as e:
    Color.p('\n[!] Interuptted, Shutting down...')
    Color.p('[!] %s' % e)
    if e == ConnectionError:
      Color.p('[!] Could be due to SMTP protocol timing out.')