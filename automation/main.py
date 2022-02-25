from lib2to3.pgen2 import driver
from selenium import webdriver

# Initialize driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://goodgame.ru/')


# Elements
streamsLink = driver.find_element_by_xpath('.//a[@href="/streams/"]')

# Actions
streamsLink.click()
print('Done')
driver.quit()