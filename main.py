from dotenv import load_dotenv
# # selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


print("....Start....")

load_dotenv()

# configure and define webDriver
options = Options()
# OpenSSL
#options.headless = True # <- Hability this opition to run in server

# difene driver and accesse website
s =Service("driver\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://www.jardineiro.net/plantas-de-a-a-z")
driver.maximize_window()