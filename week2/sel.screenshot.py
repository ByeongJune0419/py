from selenium import webdriver
import time
url = "https:/..statiz,spooki "
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
driver.get.screenshot.as_file("baseball_gamee.png")
driver.close()