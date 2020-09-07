#Ex. 1 (test if a given page is found or not)

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://abcxyz.com")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print(html.read())

try:
    html = urlopen("http://www.example.com/")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print("HTML Details")
    print(html.read())

#Ex. 2

import requests
response = requests.get("https://en.wikipedia.org/robots.txt")
test = response.text
print(test)

#Ex. 13

import requests

response = requests.get("https://analytics.usa.gov/data/live/realtime.json")
dictionary_response = response.json()
number_of_visitors = dictionary_response["data"][0]["active_visitors"]
print("number of visitors: ", number_of_visitors)


#Ex. 14

from selenium import webdriver

driver = webdriver.Chrome("C:\\voicu emil\\chromedriver\\chromedriver.exe")

driver.get('https://us-cert.cisa.gov/ncas/alerts/2020')
alarms = driver.find_element_by_xpath('/html/body/div/div[5]/div/section/div[2]/div/div/div[2]/div/ul')
all_children = alarms.find_elements_by_xpath('./*')

print("number if alarms in 2020:", len(all_children))
driver.quit()


#Ex.2

