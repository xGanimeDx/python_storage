from tkinter import *

def myClick():
    myLabel = Label(root, text='Text after click on the button')
    myLabel.grid(row=1, column=1)

def displayText():
    value = myInput.get()
    label = Label(root, text=value)
    label.grid(row=4, column=1)

# Instantiate root widget
root = Tk()
# Change the title of the root widget (read window)
root.title('TEST')

# Create a button widget and use root widget as parent for it
myButton = Button(root, text="Click me!", state='normal', command=myClick)

# Create an input widget and use root widget as parent for it
myInput = Entry(root)

displayButton = Button(root, text='Display Text From Input', command=displayText)

myButton.grid(row=0, column=0)
myInput.grid(row=1, column=0)
displayButton.grid(row=2, column=0)

root.mainloop()
