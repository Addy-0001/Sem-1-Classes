from tkinter import *
# from .form import *
root = Tk()
root.title("LBMS")
root.geometry("1920x1080")
root.resizable(False, False)
root.config(bg="black")
a = Button(root, text="North")
b = Button(root, text="East")
c = Button(root, text="South")
d = Button(root, text="West")

a.pack(side=TOP)
b.pack(side=RIGHT)
c.pack(side=BOTTOM)
d.pack(side=LEFT)


root.mainloop()
