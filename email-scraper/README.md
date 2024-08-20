<div align="center">
  <h1>Email Scraper</h1>
  Web scraping tool that extracts email addresses from a list of URLs.
</div>

## Getting Started
Follow these steps to set up and run the script on your local machine.

### Prerequisites
- Python3
- requests
- beautifulsoup4

Install these dependencies using `pip`:
```
pip install requests beautifulsoup4
```

## Usage
#### Prepare the URLs:
- Remove the old `urls.txt` file and create a new one in the project's root directory with the same name.
- Add the URLs you wish to scrape, one URL per line.

#### Run the Scraper:
```
python scraper.py
```

## Notes
- The `urls.txt` file should contain valid URLs, one per line.
- The script will append the extracted emails to `emails.txt`. If the file does not exist, it will be created.