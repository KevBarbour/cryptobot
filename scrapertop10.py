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
        txt = td.text.replace('\n', ' ').replace('*', '').strip()
        L.append(txt)
   
    F=F+1  
    if F>4:
        break

A = np.reshape(L, (5,7))    
Perm = [1,3,6,2,4,5,0]
A = A[:, Perm]
A = np.delete(A, (3,4,5,6), 1)

with open("output.txt", "w") as txt_file:
    for line in A:
        txt_file.write("#" + " ".join(line) + "\n")

T = open("output.txt", "r")
finaltweet = T.read()

tweetStr = "Todays Top 5 Crypto Coins (marketcap): \n" + finaltweet + "#cryptocurrency #crypto #blockchain #trading #money"

#twitter API commands
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
api.update_status(status=tweetStr)
print("Tweeted: " + tweetStr)