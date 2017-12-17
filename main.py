# import libraries
import urllib
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

def main():
    # find user
    user = input("What user do you want to search? ")
    print("Searching for user " + "\"" + user + "\"" + ".");
    userURL = "https://www.instagram.com/" + user
    print("Link generated \"" + userURL + "\"")

    data = getData(userURL)
    if data is None:
        return
    soup = BeautifulSoup(data, "html.parser")
    HDURL = soup.find_all("script", attrs={"type": "text/javascript"})[2]
    print(HDURL)






main()
