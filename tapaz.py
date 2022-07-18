#Libraries
from bs4 import BeautifulSoup
import requests
from pydantic import BaseModel



class Item:
    name: str
    price: float
    url: str

def getTapazItems():
  all_items = [];
  url = 'https://tap.az'
  next_url = '/elanlar/neqliyyat/aqrotexnika?p%5B899%5D=7699';
  item_length = 0;

  while (True):
    html_text = requests.get(url+next_url).text;

    soup = BeautifulSoup(html_text, 'lxml');
    endless_products = soup.find('div', {'class': 'js-endless-container products endless-products'})

    for i in endless_products.select('div[class*="products-i rounded"]'):
      print(i.find('div', {"class": "products-name"}).text);
      item = Item();
      item.name = i.find('div', {"class": "products-name"}).text;
      item.price = i.find('span', {"class": "price-val"}).text;
      item.url = url+i.find('a', {"class": "products-link"})['href'];
      all_items.append(item);
      item_length+=1;
    
    next_page = endless_products.find('div', {'class': 'pagination'});

    if(next_page):
      next_url = next_page.find(href=True)['href'];
      print(url+next_url);
    else:
      break;
    
  print("item size: " + str(item_length));
  return all_items;