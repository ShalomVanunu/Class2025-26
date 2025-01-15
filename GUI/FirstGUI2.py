from tkinter import *

app = Tk() # app object from Tkinter
app.title("My New App")
app.geometry("300x300")
app.resizable(False,False)

def click_me():
    txt.insert(INSERT,entry.get()+"\n")
    entry.delete(0, END)

def clear_me():
    txt.delete(1.0,END)

label  = Label(app, text = " Welcome Class", font=('David',20),bg="yellow")
label.pack()
button1 = Button(app, text = "Add List", command=click_me)
button1.pack()
button2 = Button(app, text = "Clear List", command=clear_me)
entry = Entry(app)
entry.pack()
button2.pack()
txt  =Text(app)
txt.pack()

app.mainloop() #  run the tKINTER OBJECT


