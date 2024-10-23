# SQL Injection Vulnerability Scanner
This script helps to identify SQL Injection vulnerabilities on websites using Google dorks. It utilizes Google search results and checks for specific SQL error messages on the websites, which may indicate a vulnerability.

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- googlesearch-python
- requests

You can install the required Python packages by running:

```
pip3 install -r requirements.txt
```

## Input parameters:

- You will be prompted to provide a Google dork. You can either input your own dork or press Enter to use the default dork (`inurl:cart.php?id=`).
- Enter the number of pages of Google search results to scan (`e.g., 5`).
Example:
```
[?] Dork: [default: inurl:cart.php?id=]  inurl:product.php?id=
[?] Total pages to search: 5
```

## Output:
```
VULN http://example.com/product.php?id=3'
Vulnerability Type: MySQL
```
If no vulnerabilities are found, no output will be shown.

## Error Handling
- If a website cannot be accessed, the script will print an error message like:
`Error accessing http://example.com/product.php?id=3'`

- If you don't have the required modules installed, you will see a message prompting you to install them:
`[!] Required modules are not installed. Run 'pip3 install -r requirements.txt'.`