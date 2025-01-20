from tkinter import *
import os

app = Tk() # app object from Tkinter
app.title("Execute Me!")
app.geometry("500x500")
app.resizable(False,False)

def  run_cmd():
        result = os.popen(enty.get()).read()
        if result:
            text.insert(END, result+"\n")
        else :
            text.insert(END, "Wrong Command"+"\n")


label = Label(app, text="Command")
label.grid(column = 0, row = 0, padx =20)
enty = Entry(app)
enty.grid(column = 1, row = 0)
button = Button(app, text="run me!", command=run_cmd)
button.grid(column = 2, row = 0)
text = Text(app,width=40,height=20, )
text.grid(column = 1, row = 1)




app.mainloop() #  run the tKINTER OBJECT