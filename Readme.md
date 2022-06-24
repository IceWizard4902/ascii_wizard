# ASCII Wizard

Python package that converts images into ASCII representation for terminals supporting `TrueColor` only.

## Acknowledgement
This project is inspired by another similar project [ASCII_Magic](https://github.com/LeandroBarone/python-ascii_magic). `ASCII_Magic` is a great choice if you still want ASCII representation on termninals not supporting TrueColor.

## TrueColor
`TrueColor` means that your terminal can display 24 bits colors (full RGB space). 

To check if your current terminal supports `TrueColor`, please check out [this excellent resource](https://github.com/termstandard/colors).

## Installation

```
pip install ascii_wizard
```

## Basic usage

```Python
import ascii_wizard 
import os 

img = ascii_wizard.AsciiWizard("doraemon.jpg")
img.colored(220, 2.2, None, None, True)
```

## Result
![](https://github.com/IceWizard4902/ascii_wizard/raw/main/example_doraemon.PNG)

# Documentation

## Initialization

Initialize the object using the default constructor.

```Python
ascii_wizard.AsciiWizard(
    path: str
)
```

where `path` is a PIL-compatible file, such as a `.jpeg` or `.png` file. See the documentation of [PIL](https://pillow.readthedocs.io/en/stable/) for other image formats.

## `grayscale()`

Convert an image into ASCII representation but with no color (basically a grayscale image).

```Python
grayscale(
    columns: int = 120, 
    width_ratio: float = 2.2,
    char: str = None,
    background: tuple = None,
    to_terminal: bool = True
) -> str
```
The method returns the ASCII representation (without color) of the image initialized using the constructor above.
- `columns (optional)`: the number of characters per row, the more columns the bigger the ASCII image.
- `width_ratio (optional)`: ASCII characters are not squares, so this adjusts the width to height ratio.
- `char (optional)`: instead of using the built-in ASCII Character Ramp, you can use a single character like `#`.
- `background (optional)`: specify the background of the image with a tuple `(r, g, b)` where `r`, `g`, `b` respectively are the RGB value of the background color.
- `to_terminal`: choose to print the ASCII image to the terminal

### Example 
**With background color**
```Python
img = ascii_wizard.AsciiWizard("elephant.jpg")
img.grayscale(150, 2.2, None, (0, 255, 255), True)
```
![](https://github.com/IceWizard4902/ascii_wizard/raw/main/example_elephant_blue.PNG)

**Without background color**
```Python
img = ascii_wizard.AsciiWizard("elephant.jpg")
img.grayscale(150, 2.2, None, None, True)
```
![](https://github.com/IceWizard4902/ascii_wizard/raw/main/example_elephant_grey.PNG)


## `colored()`

Convert an image into ASCII representation in true color. 
```Python
colored(
    columns: int = 120, 
    width_ratio: float = 2.2,
    char: str = None,
    background: tuple = None,
    to_terminal: bool = True
) -> str
```
The method returns the ASCII representation (with color) of the image initialized using the constructor above.
- `columns (optional)`: the number of characters per row, the more columns the bigger the ASCII image.
- `width_ratio (optional)`: ASCII characters are not squares, so this adjusts the width to height ratio.
- `char (optional)`: instead of using the built-in ASCII Character Ramp, you can use a single character like `#`.
- `background (optional)`: specify the background of the image with a tuple `(r, g, b)` where `r`, `g`, `b` respectively are the RGB value of the background color.
- `to_terminal`: choose to print the ASCII image to the terminal
  
## Example
```Python
img = ascii_wizard.AsciiWizard("chuamotcot.jpg")
img.colored(200, 2.2, None, None, True)
```
![](https://github.com/IceWizard4902/ascii_wizard/raw/main/example_chuamotcot.PNG)