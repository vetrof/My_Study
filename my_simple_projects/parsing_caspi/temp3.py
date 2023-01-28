from bs4 import BeautifulSoup

# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "json")
print(soup.prettify())

