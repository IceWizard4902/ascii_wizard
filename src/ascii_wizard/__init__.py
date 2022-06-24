from PIL import Image 
import os 
import sys 

__VERSION__ = 1.2

# The ASCII Character Ramp. See details at http://paulbourke.net/dataformats/asciiascii_img/
# This is a self-sourced ramp, there should be a few online
ASCII_CHAR_RAMP = " `.\'-,_:~\";!^/\\()+|><=vLc*[?xi]lTrznuJY}7ty{soj1CFkIVhae32X4ZP965qwdfUmSApEbKGHO#&%DOR8QMNBW$g@"

# Reset ANSI escape character
RESET = "\x1b[0m\n"

# Enabling 24 bit color for each ASCII character 
# ANSI escape character
COLOR = "\x1b[38;2;"
BACKGROUND = "\x1b[48;2;"

class AsciiWizard:
    def __init__(self, path):
        self.img = Image.open(path) 
    
    def grayscale(self, columns = 120, width_ratio = 2.2, char = None, background = None, to_terminal = True):
        ascii_img = to_grayscale(self.img, columns, width_ratio, char, background)
        if to_terminal:
            terminal_display(ascii_img)
        return ascii_img

    def colored(self, columns = 120, width_ratio = 2.2, char = None, background = None, to_terminal = True):
        ascii_img = to_colored(self.img, columns, width_ratio, char, background)
        if to_terminal:
            terminal_display(ascii_img)
        return ascii_img

def resize_image(img, columns, width_ratio):
    img_width, img_height = img.size
    scaling_factor = img_width * width_ratio / columns
    img_width = int(img_width * width_ratio / scaling_factor)
    img_height = int(img_height / scaling_factor)

    return img.resize((img_width, img_height))

def img_to_ascii(img, char, background, colored):
    img_width, img_height = img.size
    grayscale_img = img.convert("L")
    ascii_img = "" 
    chars = [char] if char else ASCII_CHAR_RAMP

    for h in range(img_height):
        ascii_img_line = ""

        for w in range(img_width):
            brightness = grayscale_img.getpixel((w, h)) / 255
            r, g, b = img.getpixel((w, h))[:3]
            ascii_char = chars[int(brightness * (len(chars) - 1))]

            if background:
                ascii_img_line += BACKGROUND + ";".join(str(x) for x in background) + "m"
            
            if colored:
                ascii_img_line += COLOR + ";".join(str(x) for x in (r, g, b)) + "m"
            
            ascii_img_line += ascii_char
        
        ascii_img_line += RESET 
        ascii_img += ascii_img_line
    
    return ascii_img

def to_grayscale(img, columns, width_ratio, char, background):
    resized_img = resize_image(img, columns, width_ratio)
    return img_to_ascii(resized_img, char, background, False)

def to_colored(img, columns, width_ratio, char, background):
    resized_img = resize_image(img, columns, width_ratio)
    return img_to_ascii(resized_img, char, background, True)

def terminal_display(ascii_img):
    os.system("")
    sys.stdout.write(ascii_img)