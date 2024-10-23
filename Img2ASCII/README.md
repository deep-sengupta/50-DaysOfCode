# Image to ASCII Converter
This Python program converts an image into ASCII art and saves the result to a text file. The user can specify the image file location, customize the output file name, and adjust the ASCII art dimensions.

## Requirements
- Python 3.x
- Required module: `pywhatkit`

```
pip install pywhatkit
```

## Example
When you run the program, you will be prompted to enter the following:
  - Image location: `example_image.jpg`
  - Output file name: `my_ascii_art`
  - Width: `120`
  - Height: `80`
<p>The ASCII art will be generated and saved to my_ascii_art.txt</p>

## Error Handling
- If the image file is not found, the program will prompt you to enter a valid path.
- Invalid width or height values will result in the default dimensions being used.