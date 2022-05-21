from tkinter import *
import string
from icalendar import Calendar

window=Tk()

def signedIn():

    profile = phoneNum.get()
    profile = profile.translate(profile.maketrans("", "", string.ascii_letters))

    signedInWindow = Toplevel(window)
    titlestr = "Add Deadlines: " + profile
    signedInWindow.title(titlestr)
    signedInWindow.geometry("500x400")

    titlePrompt = Label(signedInWindow, text="Enter Deadline Title: ")
    titlePrompt.place(x=50,y=30)

    titleEntry = Entry(signedInWindow)
    titleEntry.place(x=50,y=50)

    datePrompt = Label(signedInWindow, text="Enter Deadline Date:")
    datePrompt.place(x=50,y=80)

    dateEntry = Entry(signedInWindow)
    dateEntry.place(x=50,y=100)

    deadlineButton = Button(signedInWindow, text = "Add Deadline")
    deadlineButton.place(x=50,y=150)

window.title('Deadline Bot')
window.geometry("500x400")

lbl = Label(window, text="Enter Phone Number to Sign In")
lbl.place(x=50,y=30)
phoneNum = Entry(window)
phoneNum.place(x=50, y=50)

btn = Button(window, text="Sign In", fg="black", command = signedIn)
btn.place(x=50, y = 100)

def signedIn():

    profile = phoneNum.get()
    profile = profile.translate(profile.maketrans("", "", string.ascii_letters))

    signedInWindow = Toplevel(window)
    signedInWindow.title("Add Deadlines: ", profile)
    signedInWindow.geometry("500x400")

    titlePrompt = Label(signedInWindow, text="Enter Deadline Title:")
    titlePrompt.place(x=50,y=30)

    titleEntry = Entry(signedInWindow)
    titleEntry.place(x=50,y=50)

    datePrompt = Label(signedInWindow, text="Enter Deadline Date:")
    datePrompt.place(x=50,y=80)

    dateEntry = Entry(signedInWindow)
    dateEntry.place(x=50,y=100)

    deadlineButton = Button(signedInWindow, text = "Add Deadline")
    deadlineButton.place(x=50,y=150)

window.mainloop()
