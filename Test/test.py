from selenium import webdriver

def test_title():
    driver = webdriver.Chrome('chromedriver')
    driver.get("https://raison-detre.herokuapp.com")
    assert driver.title == "Raison D'être", "should be 'Raison D'être'"
    driver.quit()
 