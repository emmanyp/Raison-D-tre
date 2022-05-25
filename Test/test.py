from selenium import webdriver
import sys
import os



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def test_title():
    driver = webdriver.Chrome(resource_path('./chromedriver.exe'))
    driver.get("https://raison-detre.herokuapp.com")
    assert driver.title == "Raison D'être", "should be 'Raison D'être'"
    driver.quit()
 

