from bs4 import BeautifulSoup
import  requests
from datetime import date
from datetime import timedelta
import numpy as np
import time
import csv

def saveFile(fileName, action, dataType, data):
    with open(fileName, action, newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        if dataType == "head":
            print("Writing Head Row")
            writer.writerow(data)
        elif dataType == "body":
            print("Appending Data Rows")
            writer.writerow(data[0])
            writer.writerow(data[1])
            writer.writerow(data[2])
            writer.writerow([""])

def get_date():
    # Get today's date
    today = date.today()
    # print("Today is: ", today)
    # Yesterday date
    yesterday = today - timedelta(days = 1)
    # print("Yesterday was: ", yesterday)
    return today,yesterday

def get_gold_price():
    URL='https://www.bankbazaar.com/gold-rate-haryana.html'
    np_head=[]

    while True:
        np_data=[]
        all_rows=[]  
        r=requests.get(URL)
        soup=BeautifulSoup(r.content,'html.parser')
        table1=soup.find_all('table', class_='table table-curved tabdetails')[1]

        for Rows in table1.find_all('tr'):
            row=[]
            for item in Rows.find_all('td'):
                data=item.text
                row.append(data)
            all_rows.append(row)
        del all_rows[1:3]

        np1=np.array(all_rows)

        today,yesterday=get_date()
        for i in range(len(np1[0])):
            if np1[0][i] == 'Today':
                np1[0][i] = today
            elif np1[0][i] == "Yesterday":
                np1[0][i] = yesterday
        # print(np1)
        np1=np1.T
        # print(np1)
        if len(np_head)==0:
            np_head=np1[0]
            saveFile("newCSV.csv", 'w',"head", np_head)
        np_data=np1[1:]
        saveFile("newCSV.csv", 'a+',"body", np_data)    
        time.sleep(2) #This time wil be 84600 instead if 2 for daily rate og gold 
get_gold_price()

