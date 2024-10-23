import subprocess
import platform
import requests
import pyfiglet
import json
import os
import re

def locate_ip():
    if platform.system().lower() == 'windows':
        command = "cls"
    else:
        command = "clear"
    subprocess.call(command, shell=True)

    banner = pyfiglet.figlet_format("IP LOCATOR")
    print(banner)

    IP_PATTERN = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

    while True:
        IP_address = input("\nPlease provide a valid IP address: ")
        if IP_address.lower() == 'q':
            quit()
        if not re.match(IP_PATTERN, IP_address):
            print("The IP address you entered is not valid.")
        else:
            break

    current_dir = os.getcwd()
    folder_name = "IP_Details"
    folder_path = os.path.join(current_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename_json = os.path.join(folder_path, f"{IP_address}_info.json")
    filename_text = os.path.join(folder_path, f"{IP_address}_info.txt")

    fields = "status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,mobile,proxy,hosting,query"
    url = f"http://ip-api.com/json/{IP_address}?fields={fields}"
    response = requests.get(url)

    with open(filename_json, 'w') as ip_data_file_json:
        json.dump(response.json(), ip_data_file_json, indent=4)

    with open(filename_text, 'w') as ip_data_file_text:
        ip_data_file_text.write(response.text)

    print("IP information saved in:", folder_path)

def get_ip():
    if platform.system().lower() == 'windows':
        command = "cls"
    else:
        command = "clear"
    subprocess.call(command, shell=True)

    banner = pyfiglet.figlet_format("IP RETRIEVER")
    print(banner)

    current_dir = os.getcwd()
    folder_name = "IP_Finder"
    folder_path = os.path.join(current_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename_ip = os.path.join(folder_path, "Public_IP.txt")
    ip_finder_url = "https://api64.ipify.org?format=json"

    response = requests.get(ip_finder_url)
    IP_Address = response.text

    with open(filename_ip, 'w') as IP_Address_File:
        IP_Address_File.write(IP_Address)

    print("Public IP address saved in:", folder_path)