import sys

class Color():
  colors = {
    'W' : '\033[0m',  # white (normal)
    'R' : '\033[31m', # red
    'G' : '\033[32m', # green
    'O' : '\033[33m', # orange
    'B' : '\033[34m', # blue
    'P' : '\033[35m', # purple
    'C' : '\033[36m', # cyan
    'GR': '\033[37m', # gray
    'D' : '\033[2m'   # dims current color. {W} resets.
  }

  replacements = {
    '[+]': '{W}{D}[{W}{G}+{W}{D}]{W}',
    '[-]': '{W}{D}[{W}{R}-{W}{D}]{W}',
    '[*]': '{W}{D}[{W}{B}*{W}{D}]{W}',
    '[!]': '{W}{D}[{W}{R}!{W}{D}]{W}',
    '[?]': '{W}{D}[{W}{O}?{W}{D}]{W}'
  }

  @staticmethod
  def s(text):
    output = text
    for (key, value) in Color.replacements.items():
      output = output.replace(key, value)
    for (key, value) in Color.colors.items():
      output = output.replace('{%s}' % key, value)
    return output

  @staticmethod
  def p(text):
    sys.stdout.write(Color.s('%s\n' %text))
    sys.stdout.flush()