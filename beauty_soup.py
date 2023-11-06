#!/opt/homebrew/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen

#url = "http://olympus.realpython.org/profiles/dionysus"
url = "https://docs.rockylinux.org/books/learning_ansible/03-working-with-files/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
