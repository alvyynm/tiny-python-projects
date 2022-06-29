## About jumia price 'stalker'
This simple Python scripts gets the price of a product when you enter a Jumia link

## Logic
The project uses two modules: BeautifulSoup and urlib. 
1. urlib enables querying of the supplied link to get the full source code of the page.
2. Once done, BeautifulSoup steps in to enable querying of specific elements in the page
3. soup.findall() is used to narrow down the search to the specific class used by Jumia to display product price

## The WHY
This script is to be used to track prices of jumia products

