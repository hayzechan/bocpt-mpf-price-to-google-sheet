from crawler import get_url_content, get_fund_price, store_data_into_google_sheet
from config import Config
from apscheduler.schedulers.background import BlockingScheduler


def start_program():
    url = Config.url
    file_name = Config.file_name
    cell_range = Config.cell_range
    chrome_path = Config.chrome_path
    sheet = Config.sheet
    url_content = get_url_content(url, chrome_path)
    fund = get_fund_price(url_content)
    return store_data_into_google_sheet(file_name, sheet, cell_range, fund)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(start_program, 'interval', hour=1)
    scheduler.start()
