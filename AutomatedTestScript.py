import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\voicu emil\\chromedriver\\chromedriver.exe")

#	- Write an automated test script that:
#	1. Opens a Chrome browser instance to the URL https://www.python.org/
#	2. Navigates to Downloads -> All Releases
#	3. Displays the most recent release (first one in the table)


def displaying_most_recent_release():

    driver.get('https://www.python.org/');
    time.sleep(5) # Let the user actually see something!

    downloads = driver.find_element_by_xpath("""//*[@id="downloads"]/a""")
    allRelease = driver.find_element_by_xpath("""//*[@id="downloads"]/ul/li[1]/a""")
    ActionChains(driver).move_to_element(downloads).click(allRelease).perform()
    driver.find_element_by_xpath("""//*[@id="content"]/div/section/div[2]/ol/li[1]/span[1]""").click()

    time.sleep(5) # Let the user actually see something!

    return True

driver.quit()