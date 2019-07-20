import tkinter as tk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       def create_entry():
           print(EmpNameField.get())
           EmpNameField.delete(0, tk.END)
           print(indoorcheck.get())
           indoorcheck.set(False)
           print(EmpIndoorField.get())
           EmpIndoorField.delete(0, tk.END)
           print(outdoorcheck.get())
           outdoorcheck.set(False)
           print(EmpOutdoorField.get())
           EmpOutdoorField.delete(0, tk.END)
           print(managecheck.get())
           managecheck.set(False)
           print(EmpManageField.get())
           EmpManageField.delete(0, tk.END)

       CreateEntryPage = tk.Label(self, text="Create a new employee.", font=('Helvetica', 12))
       CreateEntryPage.place(x=10, y=10)

       EmpNameHead = tk.Label(self, text="-Employee Name (first, space, last)")
       EmpNameHead.place(x=20, y=40)

       EmpNameField = tk.Entry(self, width=30, textvariable=tk.StringVar())
       EmpNameField.place(x=30, y=60)

       ########################################################################################
       ##################################INDOOR################################################
       ########################################################################################

       EmpIndoorHead = tk.Label(self, text="indoor")
       EmpIndoorHead.place(x=50, y=90)

       indoorcheck = tk.IntVar()
       EmpIndoorCheck = tk.Checkbutton(self, variable=indoorcheck)
       EmpIndoorCheck.place(x=100, y=90)

       EmpIndoorField = tk.Entry(self, width=5)
       EmpIndoorField.place(x=160, y=90)

       EmpIndoorHours = tk.Label(self, text="hours")
       EmpIndoorHours.place(x=120, y=90)

       ########################################################################################
       ##################################OUTDOOR###############################################
       ########################################################################################

       EmpOutdoorHead = tk.Label(self, text="outdoor")
       EmpOutdoorHead.place(x=50, y=120)

       outdoorcheck = tk.IntVar()
       EmpOutdoorCheck = tk.Checkbutton(self, variable=outdoorcheck)
       EmpOutdoorCheck.place(x=100, y=120)

       EmpOutdoorField = tk.Entry(self, width=5)
       EmpOutdoorField.place(x=160, y=120)

       EmpOutdoorHours = tk.Label(self, text="hours")
       EmpOutdoorHours.place(x=120, y=120)

       ########################################################################################
       ##################################MANAGE########################################
       ########################################################################################

       EmpManageHead = tk.Label(self, text="manage")
       EmpManageHead.place(x=50, y=150)

       managecheck = tk.IntVar()
       EmpManageCheck = tk.Checkbutton(self, variable=managecheck)
       EmpManageCheck.place(x=100, y=150)

       EmpManageField = tk.Entry(self, width=5)
       EmpManageField.place(x=160, y=150)

       EmpManageHours = tk.Label(self, text="hours")
       EmpManageHours.place(x=120, y=150)

       SubmitCreateButton = tk.Button(self, text="Submit employee creation", command=create_entry)
       SubmitCreateButton.place(x=10, y=200)


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       scrollbar = tk.Scrollbar(self)
       scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

       listbox = tk.Canvas(self, yscrollcommand=scrollbar.set)
       for i in range(1000):
           listbox.insert(tk.END, str(i))
       listbox.pack(side=tk.LEFT, fill=tk.BOTH)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()