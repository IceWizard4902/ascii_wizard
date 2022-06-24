import os 
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import ascii_wizard

img = ascii_wizard.AsciiWizard("elephant.jpg")
img.grayscale(150, 2.2, None, (0, 255, 255), True)