import getpass

def createURLFile(urls):
    username = getpass.getuser()
    urlFile = open("C:/Users/" + username + "/Desktop/urls.txt","w")

    for url in urls:
        urlFile.write(url + "\n")
    urlFile.close()
    return urlFile;
