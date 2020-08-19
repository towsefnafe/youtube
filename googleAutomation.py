from selenium import webdriver
import time

search = input("What do you want to search?")

path = 'C://chromedriver.exe'
browser = webdriver.Chrome(path)

browser.get('https://www.google.com/')

searchField = browser.find_element_by_name('q')
searchField.send_keys(search)
searchField.submit()

time.sleep(10)

browser.close()
