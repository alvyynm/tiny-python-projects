from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = input("Enter your url including http/s: ")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
website = urlopen(req).read()
soup = BeautifulSoup(website, "html.parser")
links = soup.find_all('span', class_="-fs24")

for element in links:
    price = element.get_text()
    price_clean = int(price[4:].replace(",", ""))
print(f"The product costs: Ksh {price_clean:,}")
