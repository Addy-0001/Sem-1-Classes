from tkinter import * 

window = Tk()
def myClick():
    myLabel = Label(window, text="Look! I clicked a Button!!", fg="red", bg= "#000099", font=50)
    myLabel.pack()

myButton = Button(window, text="Click Me!", command=myClick, fg="blue", bg="red", font=50)
myButton.pack()

mybutton2 = Button(window, text="Don't Click Me!", state=DISABLED)
mybutton2.pack()


window.mainloop()