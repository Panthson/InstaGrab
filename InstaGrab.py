import GetURLs as urls

def main():
    user = input("What user do you want to search? ")
    if urls.userIsEmpty(user):
        print("Enter a valid user.")
        return
    print("Searching for user " + "\"" + user + "\"" + ".")
    URLList = urls.getURLs(user)
    if URLList is None:
        return
    print(URLList)
if __name__ == '__main__':
    main()
