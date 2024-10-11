# Web Scraper
This Python script scrapes all the URLs from a webpage provided by the user and stores the result in a `results.txt` file.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
```
pip3 install requests beautifulsoup4
```

## Usage
- Run the Python script:
```
python3 scraper.py
```
- When prompted, enter the URL you want to scrape.
- The script will extract all URLs from the provided webpage and save them in a file called results.txt.

## Example
```
Enter the URL: https://www.python.org
Results have been saved in results.txt
```