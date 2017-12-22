from tkinter import *
import GetURLs as urls
import DownloadPictures as dp

def getUser():
    urls.getURLs(user.get())

window = Tk()
#window.minsize(width=300, height=100)
window.resizable(width=False, height=False)

mainFrame = Frame(window, padx="10px", pady="5px")
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
user = Entry(inputFrame)
searchButton = Button(inputFrame, text="Steal Photos!", command=getUser)
error = Label(inputFrame, text="User Not Found!", font="System", fg="red")

searchButton.grid(row=0, column=1)
user.grid(row=0, column=0)
error.grid(row=1, columnspan=2)

window.mainloop()
