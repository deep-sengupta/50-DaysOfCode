# IP LOOKUP
A Python-based tool that helps you trace the geographical location of any IP address and also retrieve your current public IP address. The program allows you to save the retrieved data in JSON and plain text formats in specific folders, making it easier to analyze and access later.

## Requirements
Before running this program, ensure you have the following dependencies installed:
- Python 3.x
- requests
- pyfiglet

```
pip install requests
pip install pyfiglet
```

## Usage
After starting the program, you will be prompted with the following menu:
1. Trace an IP Address:
    - Enter `1` to locate any IP address.
    - The program will ask you to input a valid IP address.
    - The geographical details of the IP will be displayed and saved to a folder named IP_Details.

2. Retrieve Public IP:
    - Enter `2` to display your public IP address.
    - The program will save the public IP in a folder named IP_Finder.

3. Exit the Program:
    - Enter `3` to quit the application.

4. Other Commands:
    - Type `clear` to reset the screen.
    - Type `q` to cancel any ongoing operation and return to the main menu.