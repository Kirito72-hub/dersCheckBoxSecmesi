import string
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:/Users/Ahmed/AppData/Local/Google/Chrome/User Data")
options.add_argument(r'--profile-directory=Default')

class DemoCheckboxes():
    def demo_checkbox(self):
        
        driver = webdriver.Chrome(executable_path=r'C:/browser drivers/chromedriver.exe', chrome_options=options)
        driver.get("https://obs.atauni.edu.tr/moduller/sayfa/dersAlma/index")
        driver.maximize_window()
        time.sleep(2)
        while(driver.find_element(By.XPATH,"//input[@id='id_90393']").is_selected() == 0):
            driver.find_element(By.XPATH, "//input[@id='id_90393']").click()
            time.sleep(0.5)

checkbox = DemoCheckboxes()
checkbox.demo_checkbox()