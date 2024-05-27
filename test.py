import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

with requests.session().get('https://api.vvhan.com/api/hotlist/toutiao') as resp:
    data = resp.json()
    print(data['data'][6])
    url = data['data'][6]['url']
    print(url)

    chrome_options = Options()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # driver.implicitly_wait(15)

    # title = driver.title

    
    time.sleep(15)
    print(driver.page_source)


    driver.quit()



# with requests.session().get('https://www.toutiao.com/trending/7373636331018128934/?rank=21') as resp:
#     print(resp.text)