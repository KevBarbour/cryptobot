#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import sys
from twython import Twython
import numpy as np

apiKey = '...'
apiSecret = '...'
accessToken = '...'
accessTokenSecret = '...'

#BeautifulSoup scraping algorythm
url = 'https://coinmarketcap.com'
soup = BeautifulSoup(requests.get(url).text, 'lxml')
L=[]
#H =["Rank","Name","M Cap","$/1", "HURR", "DURR", "24 hr"] 
F=0

for tr in soup.select('#currencies tr'):
    if not tr.select('td'):
        continue

    for i, td in  enumerate(tr.select('td')[:7]) :
        txt = td.text.replace('\n',' ').replace('*', '').replace('%','').replace('.com','').replace('chain','').replace('coin','').strip()
        L.append(txt)
        
    #dictates how many lines will be read
    F=F+1  
    if F>99:
        break
    
    #reshapes array to only include necessary columns and re orders them
A = np.reshape(L, (100,7))    
Perm = [1,3,6,2,4,5,0]
A = A[:, Perm]
A = np.delete(A, (1,3,4,5,6), 1)

#sorting array based on percent change
A = sorted(A,key=lambda x: (float(x[1])), reverse=True)
A = A[:10]

#write table to a python file and re reads it, possibly poor method
with open("output10winners.txt", "w") as txt_file:
    for line in A:
        txt_file.write("#" + " ".join(line) + "%" + "\n" )

T = open("output10winners.txt", "r")

finaltweet = T.read()
tweetStr = "Top 10 #Crypto Winners 24hrs:" + "\n" + finaltweet

#twitter API commands
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
api.update_status(status=tweetStr)
print("Tweeted: " + tweetStr)
