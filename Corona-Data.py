from tabulate import tabulate
import os
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup 
choice=int(input('Press 1 for Statewise data and 0 for Country wise data-'))
if choice==1:
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]  
    URL = 'https://www.mohfw.gov.in/'
    
    SHORT_HEADERS = ['S.No', 'State','Confirmed','Cured','Died']  
    
    response = requests.get(URL).content  
    soup = BeautifulSoup(response, 'html.parser')  
    header = extract_contents(soup.tr.find_all('th'))  
  
    stats = []  
    all_rows = soup.find_all('tr')  
  
    for row in all_rows:  
        stat = extract_contents(row.find_all('td'))  
     
   
        if len(stat) == 6:  
             stats.append(stat)  
  
    stats[-1][0] = len(stats)  
    stats[-1][1] = "Total Infected"  
    objects = []  
    for row in stats :  
       objects.append(row[1])   
    
    y_pos = np.arange(len(objects))  
  
    performance = []  
    for row in stats[:len(stats)-1] :  
        performance.append(int(row[2]))  
  
    performance.append(int(stats[-1][2][:len(stats[-1][2])-1])) 
  
    table = tabulate(stats, headers=SHORT_HEADERS)  
  #print(table)

    plt.barh(y_pos, performance, align='center', alpha=0.5,  
                  color=(20/256.0, 10/256.0, 25/256.0),  
                   edgecolor=(106/256.0, 27/256.0, 154/256.0))  
    
    plt.yticks(y_pos, objects)  
    plt.xlim(1,performance[-1]+30000)  
    plt.xlabel('Number of Cases')  
    plt.ylabel('States')
    plt.title('Corona Virus Cases')  
    plt.show() 
else:
      co=input('Country-')
      url='https://api.covid19api.com/total/country/'+co
      r=requests.get(url)
      dic=r.json()
      confirmed=[]
      death=[]
      for i in range(len(dic)):
         confirmed.append(dic[i]['Confirmed'])
         death.append(dic[i]['Deaths'])
      x_pos = np.arange(len(dic))
      plt.xlabel('Days')
      plt.ylabel('Infected')
      plt.title('Corona Virus Cases')
      plt.plot(x_pos,confirmed)
      plt.show()
      
      

