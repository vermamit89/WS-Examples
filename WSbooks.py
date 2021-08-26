from bs4 import BeautifulSoup
import requests
import pandas as pd

URL='http://books.toscrape.com'

def request():
    r=requests.get(URL)
    return r

def B_Soup():
    R=request()
    soup=BeautifulSoup(R.text, 'html.parser')
    products=soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
   
    IMG=[]
    TITLE=[]
    PRICE=[]
    STOCK=[]

    for i in range(1,len(products)):
        img=products[i].find('img',class_='thumbnail')
        
        Prod_img=img['src']
        # print(Prod_img)
        IMG.append('http://books.toscrape.com/'+Prod_img)

        Prod_title=img['alt']
        # print(Prod_title)
        TITLE.append(Prod_title)

        Prod_price=products[i].find('p',class_='price_color').text.split('Â')[1]
        # print(Prod_price)
        PRICE.append(Prod_price)

        Prod_stock_availability=products[i].find('p',class_='instock availability').text.strip()
        # print(Prod_stock_availability)
        STOCK.append(Prod_stock_availability)
    
    return IMG,TITLE,PRICE,STOCK

def save_file():
    IMG,TITLE,PRICE,STOCK=B_Soup()
    df=pd.DataFrame(list(zip(IMG,TITLE,PRICE,STOCK)),columns=['Prod_img_url','Prod_title','Prod_price','Prod_stock_availability'],index=pd.RangeIndex(start=1, stop=20, name='index'))
    df.to_csv('WSbooks.csv')

save_file()

