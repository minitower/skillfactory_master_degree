import wget
import zipfile
import os

def get_data():
    wget.download('https://lms-cdn.skillfactory.ru/assets/courseware/v1/71b705fb3dda956399b2209697366543/asset-v1:SkillFactory+MIFIML-1sem+2024+type@asset+block/_unconv.zip', 
                  './data/data.zip')
    with zipfile.ZipFile('./data/data.zip', 'r') as zip_ref:
        zip_ref.extractall('./data')
    os.rename('./data/unconv.csv', './data/data.csv')
    os.remove('./data/data.zip')    