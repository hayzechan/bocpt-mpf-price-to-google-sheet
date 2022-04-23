from crawler import get_url_content, get_fund_price, store_data_into_google_sheet

if __name__ == '__main__':
    url = 'https://www.bocpt.com/homepage/my-choice-mpf/fund-price-enquiry/'
    file_name = 'Currency'
    cell_range = 'A1:B'
    url_content = get_url_content(url)
    fund = get_fund_price(url_content)
    store_data_into_google_sheet(file_name, cell_range, fund)
