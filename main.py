from crawler import get_url_content, get_fund_price, store_data_into_google_sheet
from config import Config

if __name__ == '__main__':
    url = Config.url
    file_name = Config.file_name
    cell_range = Config.cell_range
    sheet = Config.sheet
    url_content = get_url_content(url)
    fund = get_fund_price(url_content)
    store_data_into_google_sheet(file_name, sheet, cell_range, fund)
