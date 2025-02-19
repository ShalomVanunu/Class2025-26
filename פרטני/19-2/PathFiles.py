import os
from tkinter import *

# ליצור gui שמכניסים עליו נתיב והוא מציג את הקבצים שיש בספרייה


def main():
    def show_lists():
        file_list = ""
        try:
            os.chdir(entry.get())
            s = os.listdir()
            for object in s:
                file_list += object + "\n"
            txt.insert(INSERT, file_list)
        except:
            txt.insert(INSERT,"Path not found!!!")

    app = Tk()
    app.title("Open library")
    app.geometry("500x500")



    entry = Entry(app,width=50)
    entry.pack()

    button=Button(app, text = "Show list",command=show_lists)
    button.pack()
    txt =Text(app)
    txt.pack()

    app.mainloop()

main()
