import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\voicu emil\\chromedriver\\chromedriver.exe")

#	- Write an automated test script that:
#	1. Opens a Chrome browser instance to the URL https://www.python.org/
#	2. Navigates to Downloads -> All Releases
#	3. Displays the most recent release (first one in the table)


def displaying_most_recent_release():

    driver.get('https://www.python.org/');
    time.sleep(5) # Let the user actually see something!

    downloads = driver.find_element_by_xpath('.//li[@id="downloads"]/a')
    allRelease = driver.find_element_by_xpath('//*[@id="downloads"]/ul/li[1]/a')
    ActionChains(driver).move_to_element(downloads).click(allRelease).perform()

    recentRelease = driver.find_element_by_xpath('.//div[@class="row download-list-widget"]//ol//li[1]//span[@class="release-number"]/a')

    return (str(recentRelease.text))

print(displaying_most_recent_release())

#	- Write an automated test script that:
#		1. Opens a Chrome browser instance to the URL https://www.python.org/
#		2. In Search bar input 'decorator' and search
#		3. Open first Results link
#       4. Select from Contents 'Examples'
#		5. Verify current example count is 5

def verify_example_count(checkingNumber):

    driver.get('https://www.python.org/')
    time.sleep(5)  # Let the user actually see something!

    driver.find_element_by_xpath('.//input[@id="id-search-field"]').send_keys("decorator", Keys.ENTER)
    driver.find_element_by_xpath('.//ul[@class="list-recent-events menu"]//li[1]//h3//a').click()
    driver.find_element_by_xpath('/html/body/div/div[3]/div/section/article/div[1]/ul/li[10]/a').click()

    examples = driver.find_element_by_xpath('/html/body/div/div[3]/div/section/article/div[11]/ol')
    all_children = examples.find_elements_by_xpath('./*')

    if checkingNumber == len(all_children):

        print(f'The current example count is {checkingNumber}')
        return True

    print(f'The current example count is not {checkingNumber}')
    return  False

verify_example_count(5)