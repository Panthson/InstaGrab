from tkinter import *
import GetURLs as urls
import DownloadPictures as dp

class InstaGui:

    def __init__(self, master):
        mainFrame = Frame(master, padx="10px", pady="5px")
        titleFrame = Frame(mainFrame)
        inputFrame = Frame(mainFrame)

        mainFrame.grid()
        titleFrame.grid(row=0)
        inputFrame.grid(row=1)


        #Create and insert title
        title = Label(titleFrame,
            text="InstaGrab",
            font=("System", 20),
            pady="5px")
        title.grid()
        #Create and insert input field
        #Create and insert search button
        global user
        user = Entry(inputFrame)
        searchButton = Button(inputFrame, text="Steal Photos!", command=self.getUser)
        error = Label(inputFrame, text="User Not Found!", font="System", fg="red")

        searchButton.grid(row=0, column=1)
        user.grid(row=0, column=0)
        error.grid(row=1, columnspan=2)

    def getUser(self):
        urls.getURLs(user.get())
