from bs4 import BeautifulSoup
import requests

website = requests.get("https://tweakers.net/nieuws/")
soup = BeautifulSoup(website.content)
soup.fin
print (soup.prettify)