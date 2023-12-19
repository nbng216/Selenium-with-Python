#using option to keep the browser open.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id = 'search_query_top' or @name = 'search_query']").send_keys("T-shirt")
driver.find_element(By.XPATH, "//button[@name ='submit_search' and @class = 'btn btn-default button-search']").click()
print("code executed")

