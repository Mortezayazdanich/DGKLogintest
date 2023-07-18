from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service('/* Selenium webdriver */')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.digikala.com")
print(driver.title)


loginButton = driver.find_element(By.XPATH,
                                  "//a[contains(@href, '/users/login-register/?_back=https://www.digikala.com/')]")
loginButton.click()

print(driver.title)

nameEmail = driver.find_element(By.XPATH, "//input[@name='login[email_phone]']")
nameEmail.send_keys("Email@email.com")

submitButton = driver.find_element(By.XPATH, "//button[contains(.,'ورود به دیجی‌کالا')]")
submitButton.click()

print(driver.title)

passWord = driver.find_element(By.XPATH, "//form[@id='authForm']/div[2]/div[3]/label/div/input")
passWord.send_keys("Password")

resumeButton = driver.find_element(By.CSS_SELECTOR, ".o-btn--full-width")
resumeButton.click()

print(driver.title)

profileHeader = driver.find_element(By.CSS_SELECTOR, ".c-header__btn-profile")
profileHeader.click()

userName = driver.find_element(By.CLASS_NAME, "c-header__profile-dropdown-user-name").text
print(str(userName))
