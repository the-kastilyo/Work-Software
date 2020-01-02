# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 12:25:13 2020

@author: mcastillo
"""

import pandas as pd
import lxml.html as lh
import bs4
from bs4 import BeautifulSoup 
from io import StringIO
import re
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#hope_this_works.html
with open(r'C:\Users\mcastillo\Desktop\Loading Plan_Copy\hope_this_works.html','r',encoding="UTF8",errors='ignore') as f:
    contents = f.read()
    soup = BeautifulSoup(contents.encode("UTF8"),'lxml')
    f.close()
soups = soup.find_all('div')

div = []
divs = []
for i in soups:
    if 'listsofFAs' in i['id'].split():
        div.append((i,i['id'].split()[1]))
for i in range(len(div)):
    divs.append((div[i][1],div[i][0].text.split()[3]))
        
df = pd.DataFrame(divs, columns =['Date', 'Heat'])
df['Heat'] = df['Heat'].astype(float)
df['Heat'] = df['Heat'].apply(lambda x: x/1000)
df = df.groupby('Date')['Heat'].mean()
#df.set_index('Date',inplace =True)

df.to_excel(r'C:\Users\mcastillo\Desktop\Loading Plan_Copy\Heat_extract_unit2_HLZC4.xlsx')
#sns.set(font_scale=1.4)
#df.plot(figsize=(12, 9), linewidth=2.5, color='blue')
#plt.xlabel("Load Date", labelpad=10)
#plt.ylabel("Total Decay Heat", labelpad=10)
#plt.title("Loading Campaign", y=1.02, fontsize=20);
#df.plot()


