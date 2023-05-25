from tkinter import *
from tkinter import ttk

root = Tk()
root.title("login")
root.geometry("300x300")
root.resizable(False, False)


a = Label(root, text="Facebook")
a.pack()


def onClick(name, password):
    print(name, password)
    printname = Label(root, text=name).pack()
    printpassword = Label(root, text=password).pack()


uName = Label(root, text="UserName")
uName.pack()
uNameEntry = Entry(root)
uNameEntry.pack()

passWord = Label(root, text="Password")
passWord.pack()
passentry = Entry(root)
passentry.pack()


submitbutton = Button(root, text="Submit",
                      command=lambda: onClick(uNameEntry.get, passentry.get)).pack()

root.bind("<Return>", onClick)


root.mainloop()
