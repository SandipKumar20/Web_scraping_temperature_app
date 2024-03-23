import requests
import selectorlib
import datetime
import pytz

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url=URL, headers=HEADERS):
    """Scrape the page source from the URL"""
    response = requests.get(URL)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temp"]
    return value


def store(extracted):
    current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
    with open("data.txt", "a") as file:
        file.write(f"{current_time},{extracted}\n")


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)
