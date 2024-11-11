import wget
import zipfile
import os

def get_currency_rate():
    wget.download('https://lms.skillfactory.ru/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block@ExchangeRates.zip', 
                  './data/currency_rate.zip')
    with zipfile.ZipFile('./data/currency_rate.zip', 'r') as zip_ref:
        zip_ref.extractall('./data')
    os.rename('./data/ExchangeRates.csv', './data/currency_rate.csv')
    os.remove('./data/currency_rate.zip')    