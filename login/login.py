from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

# driver path
path = r'C:\Users\gowth\Downloads\chromedriver_win32 (2)\chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(service=service)

# Open a webpage and maximize window
driver.get("https://www.intervue.io")
driver.maximize_window()
time.sleep(7)
#click on login button
driver.find_element(By.XPATH, "//span[text()='Login']").click()
time.sleep(7)

#once clicked on login switch to new tab
driver.switch_to.window(driver.window_handles[1])

#wait until url contains /access-account
WebDriverWait(driver, 15).until(EC.url_contains("/access-account"))

#click on login button for companies
login_button = driver.find_element(By.XPATH, "//div[contains(@class, 'AccessAccount-Card Companies')]//a[contains(@class, 'AccessAccount-ColoredButton')]//div[contains(@class, 'AccessAccount-ColoredButton-Text')]")
login_button.click()

#fill username  and password
driver.find_element(By.ID, "login_email").send_keys("neha@intervue.io")
driver.find_element(By.ID, "login_password").send_keys("Ps@neha@123")

#wait for login with mail button
login_button_span = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[3]/div/div/div/div[2]/form/div[4]/div/div/span/button/span'))
)

# Scroll into view to view the button
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", login_button_span)

# Wait until button is clickable
login_button1= WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[3]/div/div/div/div[2]/form/div[4]/div/div/span/button'))
)
time.sleep(20)
login_button1.click()

#wait until it is navigated
WebDriverWait(driver, 30).until(EC.url_contains("/profile/dashboard"))
time.sleep(20)

#find searchbox
search_box = driver.find_element(By.XPATH, "//span[@class='search_placeholder' and text()='Search by candidate name, profile etc.']")
search_box.click()
search_input = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type what you want to search for']"))
)

# Type "hello" into the searchbox
search_input.send_keys("hello")
WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'SearchThrough__PlaceholderText') and contains(., 'hello')]"))
).click()
time.sleep(2)
#click on profile
WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'userAvatar') and text()='N']"))
).click()
time.sleep(2)
#click on logout button
WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
).click()


time.sleep(5)
driver.quit()
