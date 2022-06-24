import os 
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import ascii_wizard

img = ascii_wizard.AsciiWizard("doraemon.jpg")
img.colored(220, 2.2, None, (255, 255, 255), True)