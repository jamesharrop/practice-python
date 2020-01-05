'''
Exercise 17
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

# This was used during testing to save the html to a file:
# with open("nytimes.txt", "w", encoding="utf-8") as f:
#     f.write(r_html)

# with open("nytimes.txt", "r", encoding="utf-8") as f:
#     r_html = f.read()

soup = BeautifulSoup(r_html)
a = soup.select('h2')
for element in a:
    print(element.text.strip())
