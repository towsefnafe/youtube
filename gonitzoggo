import requests
from bs4 import BeautifulSoup

url = 'https://gonitzoggo.com/profile/view/towsefnafe'

r = requests.get(url).text

soup = BeautifulSoup(r, 'html.parser')

results = soup.select('td h4.align-center strong')

math = results[0].text[1:]
physics = results[1].text[1:]
print(math, physics)
