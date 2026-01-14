import requests
from bs4 import BeautifulSoup

strona = requests.get("https://www.interia.pl/?ref=s#")

soup = BeautifulSoup(strona.content, "html.parser")

print(soup.prettify())