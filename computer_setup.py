from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get('https://www.google.com/chrome/')

folder = driver.find_element('xpath', '//*[@id="js-download-hero"]')

# https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python
