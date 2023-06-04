from tkinter import *
root = Tk()
root.geometry("800x800")
root.resizable(0, 0)


def onClick():
    name = e1.get()
    password = e2.get()

    print(name, end="")
    print(password)
    Label(text=name + password).place(x=200, y=200)


a = Label(root, text="Facebook", fg="blue")
a.pack()
name = Label(root, text="Username", fg="purple")
name.place(x=89, y=55)
password = Label(root, text="Password", fg="purple")
password.place(x=92, y=78)
e1 = Entry(root)
e1.place(x=155, y=55)
e2 = Entry(root)
e2.place(x=155, y=79)
submit = Button(root, text="Login", bg="white", command=onClick)
root.bind(
    '<Return>', onClick
)
submit.place(x=187, y=110)
root.mainloop()
