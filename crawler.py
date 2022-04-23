import gspread
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_url_content(url):
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
    chrome_driver_binary = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=chrome_driver_binary, options=options)
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    return soup


def get_fund_price(soup: BeautifulSoup):
    html_tag_finder = soup.find_all('div', attrs={'style': 'display: table-row;', 'class': 'fund-item'})
    price = []
    for i in html_tag_finder:
        tag = i.find_all('div')
        for j in tag:
            j.find('div')
            get_text = j.get_text()
            try:
                float(get_text)
                price.append(float(get_text))
            except Exception:
                ...
    return price_to_nested_list(price)


def price_to_nested_list(price):
    return [price[x:x + 2] for x in range(0, len(price), 2)]


def store_data_into_google_sheet(file: str, cell_range: str, price_list):
    gc = gspread.service_account(filename='cred.yml')
    sh = gc.open(file).sheet1
    sh.update(cell_range, price_list)
