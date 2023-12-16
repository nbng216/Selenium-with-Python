# To verify the numbers of sliders in the page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://www.automationpractice.pl/index.php")

# locating the slider element

slides = driver.find_elements(By.CLASS_NAME, "homeslider-container")
for i in slides:
    print(i)

# To find number of links present inside page use below line
# slides = driver.find_elements(By.TAG_NAME, "a")

print(len(slides))
