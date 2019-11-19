from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options


opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(
    firefox_binary=binary, executable_path=r'C:\\geckodriver.exe', options=opts
)
driver.get('https://duckduckgo.com')
search_form = driver.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()
results = driver.find_elements_by_class_name('result')
print(results[0].text)
driver.close()
