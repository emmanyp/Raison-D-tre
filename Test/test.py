from selenium import webdriver

#Grabbing the Browser
driver = webdriver.Chrome()
#Opening the Browser for the app
driver.get("http://127.0.0.1:8000/")

assert driver.title == "Raison D'être"

#Close the Browser
driver.quit()
