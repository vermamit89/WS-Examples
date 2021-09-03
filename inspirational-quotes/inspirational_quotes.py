from bs4 import BeautifulSoup
import requests
import humanize
import pandas as pd


URL='https://www.passiton.com/inspirational-quotes'

def Request():
    r=requests.get(URL)
    return r
    # print(r.text)

def Soup():
    R=Request()
    soup=BeautifulSoup(R.text,'lxml')
    # print(soup.prettify())
    quotes=soup.find_all('div', class_="col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top")
    # print(quote.prettify())
    quoteslist=[]
    quotelinks=[]
    for quote in quotes:
        Q_img=quote.find('img', class_='margin-10px-bottom shadow')
        Q_img_lines=Q_img['alt'].split('#')[0]
    
        links=quote.find('a')
        Q_links=links['href']

        quotelinks.append("https://passiton.com"+Q_links)
        quoteslist.append(Q_img_lines)

    return quotelinks,quoteslist




# for i in range(len(quoteslist)):
    # print(f'{humanize.ordinal(i)} quote is :- {quoteslist[i]}')
    # print(f'{humanize.ordinal(i)} link is :- https://passiton.com{quotelinks[i]}\n\n')
    

def Save_File():
    quotelinks,quoteslist=Soup()
    df=pd.DataFrame(list(zip(quoteslist,quotelinks)),columns=['Qoutes','Links'],index=pd.RangeIndex(start=1, stop=33, name='index'))
    df.to_csv('F:\python tuorials\Web scraping\WebScraping-Examples/inspirational_quotes.csv')



Save_File()
