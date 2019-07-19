import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.click_count = 0

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        self.click_count += 1
        print("you've clicked " +str(self.click_count) + " times")
        self.create_widgets()



root = tk.Tk()
app = Application(master=root)
app.mainloop()


