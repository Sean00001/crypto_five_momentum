import pandas as pd

def getData(the_code):
    def clearSpace(value):
        return value.strip()

    price_data = pd.read_csv('./taiwan-index-price-data.txt', encoding='cp950')
    price_data['證券代碼'] = price_data['證券代碼'].apply(clearSpace)
    price_data['簡稱'] = price_data['簡稱'].apply(clearSpace)
    target_data = price_data[price_data['證券代碼'] == the_code]
    target_data['ret'] = target_data['收盤價(元)'].diff(1)/target_data['收盤價(元)'].shift(1)
    target_data = target_data.dropna()
    target_data = target_data.reset_index(drop=True)
    return target_data