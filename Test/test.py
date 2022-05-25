from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_title():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://raison-detre.herokuapp.com")
    assert driver.title == "Raison D'être", "should be 'Raison D'être'"
    driver.quit()
 