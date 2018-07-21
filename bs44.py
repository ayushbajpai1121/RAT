import bs4
from bs4 import BeautifulSoup
import urllib3
import requests
import pymongo

print("Input movie name")
str1=input()
print("Input Year")
str2=input()
html_doc="https://downloadming.pro/"+str1+"-"+str2+"-mp3-songs"
r=requests.get(html_doc)
data=r.text
soup = BeautifulSoup(data,'html.parser')

print(soup.title)

#print(soup.find_all('table'))
tag=soup.table
#print(tag)
tag1=tag.contents[1]#referring to tbody tag
ln=len(tag1.contents)#findinglength to iterate

for i in range(3,ln-3,2):
    tag2=tag1.contents[i]#finding tr tag for each song
    xy=tag2.find_all('a')
    print(tag1.contents[i].contents[1].text)#printing song name and singers
    #print(xy,end="\n\n")
    link1=xy[0].get('href')
    print("128 kbps:",link1)
    link2=xy[1].get('href')
    print("300 kbps:",link2)
    


#for link in tag2:
    #print(link)
#for i in tag2.children:
 #   print(i)
    
#for child in tag1.descendants:
    
    #print(child)
    
#print(soup.get_text())
#print(soup.find_all('table'))

