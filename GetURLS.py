# import libraries
import json
import urllib
import DownloadPictures as dp
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getData(url):
    try:
        data = urlopen(url)
    except urllib.error.HTTPError as e:
        return
    return data

def getURLs():
    # find user
    user = "panthson"
    userURL = "https://www.instagram.com/" + user

    data = getData(userURL)
    if data is None:
        data = invalidUserInput(data)
        if data is None:
            return
    soup = BeautifulSoup(data, "html.parser")

    #Get JSON object from HTML
    JSONHTML = soup.find_all("script", attrs={"type": "text/javascript"})[2]
    JSONHTML = str(JSONHTML)
    JSONHTML = JSONHTML.replace("<script type=\"text/javascript\">window._sharedData = ", "")
    JSONHTML = JSONHTML.replace(";</script>", "")

    JSONObj = json.loads(JSONHTML)
    # for i in JSONObj["entry_data"]["ProfilePage"][0]["user"]["media"]["nodes"]:
    #     print(i)
    # print(len(JSONObj["entry_data"]["ProfilePage"][0]["user"]["media"]["nodes"]))
    # print("Not found yet")
    urls = ["facebook.com", "instagram.com"]
    dp.createURLFile(urls)

def invalidUserInput(data):
    while data is None:
        print("User not found!")
        check = input("Would you like to search again? (y/n) ")
        while check is not "y" and check is not "n":
            print("Invalid input.")
            check = input("Would you like to search again? (y/n) ")
            if check is "y":
                user = input("What user do you want to search? ")
                userURL = "https://www.instagram.com/" + user
                data = getData(userURL)
                return data
            if check is "n":
                return
        if check is "y":
            user = input("What user do you want to search? ")
            userURL = "https://www.instagram.com/" + user
            data = getData(userURL)
            return data
        if check is "n":
            return

def userIsEmpty(user):
    if len(user) is 0:
        return True;
    for i in user:
        if i is not " ":
            return False
    return True
