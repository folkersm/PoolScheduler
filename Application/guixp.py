import tkinter
import random
import WritingToFile as wr


def create_entry():
    print(EmpNameField.get())
    EmpNameField.delete(0, tkinter.END)
    print(indoorcheck.get())
    indoorcheck.set(False)
    print(EmpIndoorField.get())
    EmpIndoorField.delete(0, tkinter.END)
    print(outdoorcheck.get())
    outdoorcheck.set(False)
    print(EmpOutdoorField.get())
    EmpOutdoorField.delete(0, tkinter.END)
    print(managecheck.get())
    managecheck.set(False)
    print(EmpManageField.get())
    EmpManageField.delete(0, tkinter.END)

root = tkinter.Tk()
root.title("Pool Scheduler")
root.geometry("375x250")
CreateEntryPage = tkinter.Label(root, text="Create a new employee.", font=('Helvetica', 12))
CreateEntryPage.place(x=10, y=10)

EmpNameHead = tkinter.Label(root, text = "-Employee Name (first, space, last)")
EmpNameHead.place(x=20, y=40)

EmpNameField = tkinter.Entry(root, width = 30, textvariable = tkinter.StringVar())
EmpNameField.place(x=30, y=60)

########################################################################################
##################################INDOOR################################################
########################################################################################

EmpIndoorHead = tkinter.Label(root, text = "indoor")
EmpIndoorHead.place(x=50, y=90)

indoorcheck = tkinter.IntVar()
EmpIndoorCheck = tkinter.Checkbutton(root, variable=indoorcheck)
EmpIndoorCheck.place(x=100, y=90)

EmpIndoorField = tkinter.Entry(root, width = 5)
EmpIndoorField.place(x=160, y=90)

EmpIndoorHours = tkinter.Label(root, text = "hours")
EmpIndoorHours.place(x=120, y=90)

########################################################################################
##################################OUTDOOR###############################################
########################################################################################

EmpOutdoorHead = tkinter.Label(root, text = "outdoor")
EmpOutdoorHead.place(x=50, y=120)

outdoorcheck = tkinter.IntVar()
EmpOutdoorCheck = tkinter.Checkbutton(root, variable=outdoorcheck)
EmpOutdoorCheck.place(x=100, y=120)

EmpOutdoorField = tkinter.Entry(root, width = 5)
EmpOutdoorField.place(x=160, y=120)

EmpOutdoorHours = tkinter.Label(root, text = "hours")
EmpOutdoorHours.place(x=120, y=120)

########################################################################################
##################################MANAGE########################################
########################################################################################

EmpManageHead = tkinter.Label(root, text = "manage")
EmpManageHead.place(x=50, y=150)

managecheck = tkinter.IntVar()
EmpManageCheck = tkinter.Checkbutton(root, variable=managecheck)
EmpManageCheck.place(x=100, y=150)

EmpManageField = tkinter.Entry(root, width = 5)
EmpManageField.place(x=160, y=150)

EmpManageHours = tkinter.Label(root, text = "hours")
EmpManageHours.place(x=120, y=150)


SubmitCreateButton = tkinter.Button(root, text = "Submit employee creation", command = create_entry)
SubmitCreateButton.place(x=10, y=200)

root.iconbitmap(r'C:\Users\Max\Desktop\Programz\Scheduler\Application\beachb.ico')

root.mainloop()
