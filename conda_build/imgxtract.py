
import requests
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def imgxract():
    i=1
    def make_soup(url):
        thepage=urllib.request.urlopen(url)
        soupdata=BeautifulSoup(thepage,"html.parser")
        return soupdata

    Link_input=input("Enter Url:-")
    soup=make_soup(Link_input)
    for img in soup.findAll('img'):
    #print(img)
    #print(img.get('src'))
        temp=img.get('src')
        if temp[ :1]=="/":
           image=Link_input+temp
        else:
          image=temp
        #print(image)
    
        nametemp=img.get('alt')
        if len(nametemp)==0:
           filename=str[i]
           i=i+1
        else:
           filename=nametemp
    
        imagefile=open(filename+".jpeg",'wb')
        imagefile.write(urllib.request.urlopen(image).read())
        imagefile.close()
            