import tkinter as tk
import WritingToFile as wr
import sqlite3 as sql

deletecount = 0

class AutoScrollbar(tk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
            tk.Scrollbar.set(self, lo, hi)

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
           wr.insert_into_db(
               EmpNameField.get().split()[0], EmpNameField.get().split()[1],
               indoorcheck.get(), outdoorcheck.get(), managecheck.get(),
               EmpManageField.get() + EmpIndoorField.get() + EmpOutdoorField.get()
           )
           EmpNameField.delete(0, tk.END)
           indoorcheck.set(False)
           EmpIndoorField.delete(0, tk.END)
           outdoorcheck.set(False)
           EmpOutdoorField.delete(0, tk.END)
           managecheck.set(False)
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

       self.refresh()

   def refresh(self):
       i_list = []

       conn = sql.connect(r'Schedulerdatabase.db')
       with conn as c:
           c = conn.cursor()
           id_s = c.execute("SELECT id FROM employee")
           id_list = id_s.fetchall()
       for id in id_list:
           i_list.append(id[0])

       vscrollbar = AutoScrollbar(self)
       vscrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)
       hscrollbar = AutoScrollbar(self, orient=tk.HORIZONTAL)
       hscrollbar.grid(row=1, column=0, sticky=tk.E + tk.W)

       canvas = tk.Canvas(self,
                          yscrollcommand=vscrollbar.set,
                          xscrollcommand=hscrollbar.set)
       canvas.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

       vscrollbar.config(command=canvas.yview)
       hscrollbar.config(command=canvas.xview)

       # make the canvas expandable
       self.grid_rowconfigure(0, weight=1)
       self.grid_columnconfigure(0, weight=1)

       #
       # create canvas contents

       frame = tk.Frame(canvas)
       frame.rowconfigure(1, weight=1)
       frame.columnconfigure(1, weight=1)

       conn = sql.connect(r'Schedulerdatabase.db')
       c = conn.cursor()
       dataCopy = c.execute("select count(*) from employee")
       values = dataCopy.fetchone()

       print(values[0])

       def delete(id):
           def deledelete():
               global deletecount
               if deletecount < 15:

                   wr.delete(id)
                   self.refresh()
                   root.destroy()
                   deletecount += 1
                   print("deletion number: " + str(deletecount))
               else:
                   root.destroy()
                   box = tk.Tk()
                   box.geometry("300x200+250+250")
                   warning = tk.Label(box, text = "Cannot manually delete more than 14 employees per session. \n"
                                                  "If you want to delete more, you have to restart \n"
                                                  "the program and delete up to 14 more. Sorry. \n"
                                                  "Contact and nag Max Folkers if you want this fixed.")
                   warning.pack()
           print(id)
           root = tk.Tk()
           root.geometry("200x150+250+250")
################################################################update v looks###########################################################
           yesbut = tk.Button(root,
                              text="YES",
                              fg="green",
                              command=lambda : deledelete())
           yesbut.pack(side=tk.LEFT)
           nobut = tk.Button(root,
                              text="NO",
                              fg="red",
                              command=root.destroy)
           nobut.pack(side=tk.LEFT)
################################################################update ^ looks###########################################################
           root.mainloop()



       for i in range(values[0]):
           emp = wr.read_table(i_list[i])

           label = tk.Label(frame, text = emp[2] + ',' +emp[1] + ' id:' + str(emp[0]))
           label.grid(row=i, column=1, sticky='news')
           button = tk.Button(frame, text = 'delete', command=lambda i=i_list[i]: delete(i))
           button.grid(row=i, column=2, sticky='news')


       canvas.create_window(0, 0, anchor=tk.NW, window=frame)

       frame.update_idletasks()

       canvas.config(scrollregion=canvas.bbox("all"))




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
    self = tk.Tk()
    main = MainView(self)
    main.pack(side="top", fill="both", expand=True)
    self.wm_geometry("400x400")
    self.mainloop()