# импортируем модули и отдельные классы

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_private_page():
    """
    Positive test case of the private page
    """
	
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") 
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions") 
	
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    url = "https://lieders.ru" # адрес моей предполагаемой странички
    driver.get(url=url)
		# ищем по селектору элемент на странице, где спрятана ссылка на гитхаб
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='tli:nth-child(3)']")
    element.click()
     #ищем на странице селектор города где я живу на гитхабе
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='li.vcard-detail.pt-1.hide-sm.hide-md']")		
		# проверяем соответствие
    assert text == 'St.Petersburg', "Unexpected text"