from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\\chromedriver.exe")
#driver.implicitly_wait(15) #implicit wait

driver.get("https://164.92.150.242/staff/staff")
driver.maximize_window()
driver.find_element("xpath", ' //*[@id="details-button"]').click()

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle
driver.find_element(By.LINK_TEXT, "Proceed to 164.92.150.242 (unsafe)").click()
driver.find_element("xpath", '//*[@id="root"]/div/div/button').click()
time.sleep(5)

# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

# change the control to signin page
driver.switch_to.window(login_page)

# enter the email
driver.find_element("xpath", '//*[@id="i0116"]').send_keys("svc-miogsims@kpc.co.ke")
time.sleep(10)

#Click on next
driver.find_element("xpath", '//*[@id="idSIButton9"]').click()
time.sleep(10)

#enter password
driver.find_element("xpath", '//*[@id="i0118"]').send_keys("Lgemo!4745")
time.sleep(10)

#Click on signin
driver.find_element("xpath", '//*[@id="idSIButton9"]').click()
time.sleep(10)

driver.find_element("xpath", '//*[@id="idSIButton9"]').click()
time.sleep(30)

# closing the window
driver.quit()