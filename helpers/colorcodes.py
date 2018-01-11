# vim: fileencoding=utf-8
"""
Facilitates printing ANSI colors on Unix consoles. Use Colorama on Windows.

Source: https://gist.github.com/4007035
"""
import subprocess

class Colorcodes(object):
    """
    Provides ANSI terminal color codes which are gathered via the ``tput``
    utility. That way, they are portable. If there occurs any error with
    ``tput``, all codes are initialized as an empty string.
    The provides fields are listed below.

    Control:
      - bold
      - underline
      - reset

    Colors:
      - red
      - green
      - yellow
      - blue
      - magenta
      - cyan
      - white

    :license: MIT
    """
    def __init__(self):
        try:
            self.bold = subprocess.check_output("tput bold".split()).decode('utf-8')
            self.ul = subprocess.check_output("tput sgr 0 1".split()).decode('utf-8')
            self.reset = subprocess.check_output("tput sgr0".split()).decode('utf-8')

            self.red = subprocess.check_output("tput setaf 1".split()).decode('utf-8')
            self.green = subprocess.check_output("tput setaf 2".split()).decode('utf-8')
            self.yellow = subprocess.check_output("tput setaf 3".split()).decode('utf-8')
            self.blue = subprocess.check_output("tput setaf 4".split()).decode('utf-8')
            self.magenta = subprocess.check_output("tput setaf 5".split()).decode('utf-8')
            self.cyan = subprocess.check_output("tput setaf 6".split()).decode('utf-8')
            self.white = subprocess.check_output("tput setaf 7".split()).decode('utf-8')

        except subprocess.CalledProcessError as e:
            self.bold = ""
            self.ul = ""
            self.reset = ""

            self.red = ""
            self.green = ""
            self.yellow = ""
            self.blue = ""
            self.magenta = ""
            self.cyan = ""
            self.white = ""


_c = Colorcodes()

