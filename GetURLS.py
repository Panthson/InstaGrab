# import libraries
import json
import unicodedata
import urllib
import sys

from urllib.request import urlopen
from bs4 import BeautifulSoup

def getData(url):
    try:
        data = urlopen(url)
    except urllib.error.HTTPError as e:
        print("Errored!")
        if e.code == 404:
            print("User not found!")
        return
    return data

def removeEmojis(string):
    print(string.find("\u"))

def getURLs():
    # find user
    user = input("What user do you want to search? ")
    print("Searching for user " + "\"" + user + "\"" + ".");
    userURL = "https://www.instagram.com/" + user
    print("Link generated \"" + userURL + "\"")

    data = getData(userURL)
    if data is None:
        return

    soup = BeautifulSoup(data, "html.parser")

    #Get JSON object from HTML
    JSONHTML = soup.find_all("script", attrs={"type": "text/javascript"})[2]
    JSONHTML = str(JSONHTML)
    JSONHTML = JSONHTML.replace("<script type=\"text/javascript\">window._sharedData = ", "")
    JSONHTML = JSONHTML.replace(";</script>", "")
    JSONHTML = removeEmojis(JSONHTML) #Removed Unicode Characters
    print(JSONHTML)

    #print(JSONHTML)
    JSONObj = json.loads(JSONHTML)
    #print(JSONObj)


getURLs()
