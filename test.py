
from bs4 import BeautifulSoup
import requests
scraped = 'https://www.shoppingmap.it/negozi?page=1'
round = 1

html_text = requests.get(scraped).text
soup = BeautifulSoup(html_text, 'lxml')
shop = soup.find_all('div', class_='title desktop-only')
# print(shop)
while (round <= 5):
    while (len(shop) > 1):
        new_shop1 = shop.pop(0)
        new_shop2 = shop.pop(0)
        new_shop3 = shop.pop(0)
        new_shop4 = shop.pop(0)
        new_shop5 = shop.pop(0)
        new_shop6 = shop.pop(0)
        new_shop7 = shop.pop(0)
        new_shop8 = shop.pop(0)
        new_shop9 = shop.pop(0)
        new_shop10 = shop.pop(0)
        print(new_shop1.text)
        print(new_shop2.text)
        print(new_shop3.text)
        print(new_shop4.text)
        print(new_shop5.text)
        print(new_shop6.text)
        print(new_shop7.text)
        print(new_shop8.text)
        print(new_shop9.text)
        print(new_shop10.text)

        testSite = scraped.split('=')
        x = testSite.pop(1)
        y = int(x) + 1
        z = str(y)
        newSite = testSite.append(z)
        scraped = '='.join(testSite)
        print(scraped)
    round += 1
    print(round)
