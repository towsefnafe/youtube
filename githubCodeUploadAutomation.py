#import
from selenium import webdriver

path = 'C://chromedriver.exe'
browser = webdriver.Chrome(path)

browser.get('https://github.com/login')

userName = browser.find_element_by_xpath('//*[@id="login_field"]')
userName.send_keys('towsefnafe')

passwordInput = browser.find_element_by_xpath('//*[@id="password"]')
password = open('password.txt', 'r')
passwordInput.send_keys(password.read())
passwordInput.submit()

browser.get('https://github.com/towsefnafe/youtube/new/master')

fileName = input()

try:
    title = browser.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[3]/div/div/form[2]/div[1]/span/input')
        title.send_keys(fileName)
            code = open(fileName, 'r')
                codeInput = browser.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[3]/div/div/form[2]/div[5]/div[2]/div/div[5]/div[1]/div/div/div/div[5]/div/pre')
                    codeInput.send_keys(code.read())
                        submitBtn = browser.find_element_by_xpath('//*[@id="submit-file"]')
                            submitBtn.click()
                            except:
                                print("Something wrong")
