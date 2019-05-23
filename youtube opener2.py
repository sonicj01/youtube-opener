import webbrowser
from bs4 import BeautifulSoup
import urllib.request
import string
import requests
#this variable is created so that the title of the video can be combined
#with the link in a way which youtube will accept
url=("https://www.youtube.com/results?search_query=")
search=input("what is the title of the video?")
#this replaces the spaces in the title with the plus sign
#which means you don't have to do it manually.
url+=search.replace(" ","+")
#this requests the html of the search results page to find the link to the video
beforeSoup=urllib.request.urlopen(url).read()
afterSoup=BeautifulSoup(beforeSoup)
Links=( )
z=0
#this finds all links with the class 'a'
linkList=list(Links)
for link in afterSoup.find_all('a'):
    #this adds them to a list, so that the program can find the right one.
    linkList.append(link.get('href'))
#this variable allows the program to format the link to open properly
yt="www.youtube.com"
y=0
#this scans through all of the links the program finds so it can find the right one
#I didn't use "for x in linklist" beause then it might find multiple links and
#open them all
for x in range(len(linkList)):
    #this tests if /watch is in the result, if it it that means that it is
    #a video link
    if "/watch" in linkList[y]:
        #this combines the /watch part with the "youtube.com" part
        yt+=(linkList[y])
        #this opens the link
        webbrowser.open_new(yt)
        break
    else:
        print("nope!")
        
    
