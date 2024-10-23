import pywhatkit as kt
import os

def get_user_inputs():
    img_loc = input("Enter the image location: ")
    while not os.path.isfile(img_loc):
        print("File not found! Please enter a valid file path.")
        img_loc = input("Enter the image location: ")

    output_file = input("Enter the output file name (without extension, default is 'ascii_text'): ") or "ascii_text"
    width = input("Enter the desired width of the ASCII art (default is 100): ") or 100
    height = input("Enter the desired height of the ASCII art (default is 100): ") or 100

    try:
        width = int(width)
        height = int(height)
    except ValueError:
        print("Invalid width or height input! Setting default values (100x100).")
        width, height = 100, 100

    return img_loc, output_file, width, height

def image_to_ascii(img_loc, output_file, width, height):
    try:
        kt.image_to_ascii_art(img_loc, f"{output_file}.txt")
        print(f"ASCII art saved to {output_file}.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    img_loc, output_file, width, height = get_user_inputs()
    image_to_ascii(img_loc, output_file, width, height)