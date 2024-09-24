import pywhatkit
from datetime import datetime
import pyautogui
import time
import keyboard

now = datetime.now()
mobile = input('Enter Mobile No (with country code): ')
message = input('Enter your message: ')
hour = int(input('Enter hour (24-hour format): '))
minute = int(input('Enter minute: '))

def send_message():
    pywhatkit.sendwhatmsg(mobile, message, hour, minute)
    time.sleep(15)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')

def stop_bot():
    if keyboard.is_pressed('esc'):
        exit()

while True:
    send_message()
    stop_bot()