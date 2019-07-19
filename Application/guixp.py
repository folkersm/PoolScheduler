import tkinter
import random
import WritingToFile as wr

def create_entry():
    print('testytesty')



root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x250")
CreateEntryPage = tkinter.Label(root, text="THis is the create employee page", font=('Helvetica', 12))
CreateEntryPage.pack()
EmpNameField = tkinter.Entry(root)
EmpNameField.pack()
EmpNameButton = tkinter.Button()
root.mainloop()
