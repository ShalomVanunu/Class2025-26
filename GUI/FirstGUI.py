from tkinter import *

app = Tk() # app object from Tkinter
app.title("My New App")
app.geometry("300x300")
app.resizable(False,False)

label  = Label(app, text = " Welcome Class", font=('David',20),bg="yellow")
label.grid(column=3, row = 2)
button1 = Button(app, text = "Click Me1!")
button1.grid(column=2, row = 3)
button2 = Button(app, text = "Click Me2!")
button2.grid(column=1, row = 4)

app.mainloop() #  run the tKINTER OBJECT


