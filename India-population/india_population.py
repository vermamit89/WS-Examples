from bs4 import BeautifulSoup
import requests
import csv
import os

def get_url():
    url="https://www.worldometers.info/world-population/india-population/"
    headers={ 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4603.0 Safari/537.36'}
    r =requests.get(url)
    return r

def bsoup():
    r=get_url() 
    soup=BeautifulSoup(r.text,'html.parser')
    table=soup.find('table',class_="table table-striped table-bordered table-hover table-condensed table-list")
    



def get_table():
    table=bsoup()
    all_rows=[]
    for rows in table.find_all('tr'):
        each_row=[]
        for heads in rows.find_all('th'):
            head=heads.text
            each_row.append(head)
        for row in rows.find_all('td'):
            data=row.text
            each_row.append(data)
        all_rows.append(each_row)
    row_heads,*row_data=all_rows
    return row_heads,row_data

def save_file():
    row_heads,row_data=get_table()
    file_name = os.path.abspath('india_population3.csv')
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        print("Writing Head Row")
        writer.writerow(row_heads)
        print("Appending Data Rows")
        writer.writerows(row_data)

save_file()











