# import tkinter as tk
#
#
# # ************************
# # Scrollable Frame Class
# # ************************
# class ScrollFrame(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)  # create a frame (self)
#
#         self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")  # place canvas on self
#         self.viewPort = tk.Frame(self.canvas,
#                                  background="#ffffff")  # place a frame on the canvas, this frame will hold the child widgets
#         self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)  # place a scrollbar on self
#         self.canvas.configure(yscrollcommand=self.vsb.set)  # attach scrollbar action to scroll of canvas
#
#         self.vsb.pack(side="right", fill="y")  # pack scrollbar to right of self
#         self.canvas.pack(side="left", fill="both", expand=True)  # pack canvas to left of self and expand to fil
#         self.canvas.create_window((4, 4), window=self.viewPort, anchor="nw",  # add view port frame to canvas
#                                   tags="self.viewPort")
#
#         self.viewPort.bind("<Configure>",
#                            self.onFrameConfigure)  # bind an event whenever the size of the viewPort frame changes.
#
#     def onFrameConfigure(self, event):
#         '''Reset the scroll region to encompass the inner frame'''
#         self.canvas.configure(scrollregion=self.canvas.bbox(
#             "all"))  # whenever the size of the frame changes, alter the scroll region respectively.
#
#
# # ********************************
# # Example usage of the above class
# # ********************************
#
# class Example(tk.Frame):
#     def __init__(self, root):
#         tk.Frame.__init__(self, root)
#         self.scrollFrame = ScrollFrame(self)  # add a new scrollable frame.
#
#         # Now add some controls to the scrollframe.
#         # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
#         for row in range(100):
#             a = row
#             tk.Label(self.scrollFrame.viewPort, text="%s" % row, width=3, borderwidth="1",
#                      relief="solid").grid(row=row, column=0)
#             t = "this is the second column for row %s" % row
#             tk.Button(self.scrollFrame.viewPort, text=t, command=lambda x=a: self.printMsg("Hello " + str(x))).grid(
#                 row=row, column=1)
#
#         # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
#         self.scrollFrame.pack(side="top", fill="both", expand=True)
#
#     def printMsg(self, msg):
#         print(msg)
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     Example(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()
# import tkinter as tk
#
# class AutoScrollbar(tk.Scrollbar):
#     # a scrollbar that hides itself if it's not needed.  only
#     # works if you use the grid geometry manager.
#     def set(self, lo, hi):
#         if float(lo) <= 0.0 and float(hi) >= 1.0:
#             # grid_remove is currently missing from Tkinter!
#             self.tk.call("grid", "remove", self)
#         else:
#             self.grid()
#             tk.Scrollbar.set(self, lo, hi)
#     # def pack(self, **kw):
#     #     raise TclError, "cannot use pack with this widget"
#     # def place(self, **kw):
#     #     raise TclError, "cannot use place with this widget"
#
#
# root = tk.Tk()
#
# vscrollbar = AutoScrollbar(root)
# vscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
# hscrollbar = AutoScrollbar(root, orient=tk.HORIZONTAL)
# hscrollbar.grid(row=1, column=0, sticky=tk.E+tk.W)
#
# canvas = tk.Canvas(root,
#                 yscrollcommand=vscrollbar.set,
#                 xscrollcommand=hscrollbar.set)
# canvas.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
#
# vscrollbar.config(command=canvas.yview)
# hscrollbar.config(command=canvas.xview)
#
# # make the canvas expandable
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
#
# #
# # create canvas contents
#
# frame = tk.Frame(canvas)
# frame.rowconfigure(1, weight=1)
# frame.columnconfigure(1, weight=1)
#
# rows = 77
# for i in range(1,rows):
#     for j in range(1,3):
#         button = tk.Button(frame, padx=7, pady=7, text="[%d,%d]" % (i,j))
#         button.grid(row=i, column=j, sticky='news')
#
# canvas.create_window(0, 0, anchor=tk.NW, window=frame)
#
# frame.update_idletasks()
#
# canvas.config(scrollregion=canvas.bbox("all"))
#
# root.mainloop()
# import sqlite3 as sql
# conn = sql.connect(r'Schedulerdatabase.db')
# c = conn.cursor()
# dataCopy = c.execute("select count(*) from employee")
# values = dataCopy.fetchone()
# print(values[0])

import math
import os
import random
import re
import sys


#
# Complete the 'alphaBeta' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY pile as parameter.
#
#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'nuclearFusion' function below.
#
# The function accepts INTEGER_ARRAY elements as parameter.
#
#
def nuclearFusion(elementss):
    elements = []
    winners = []
    losers = []
    for i in elementss:
        elements.append(i)
    def is_end(list, n):
        for i in range(len(list)):
            if n == list[i]:
                return False
            else:
                pass
        return True
    def check_ends(list):
        out = []
        for x in range(len(list)):
            if is_end(elements, x+2):
                out.append(x)
        outt = []
        for x in range(len(out)):
            if elements[out[x]] not in outt:
                outt.append(elements[out[x]])
        return outt

    def run_connects(list):
        cur_lose = []
        connects = check_ends(list)
        for i in range(len(connects)):
            end_nodes = []
            for j in range(len(list)):
                if connects[i] == list[j]:
                    end_nodes.append(j + 2)
            print(len(end_nodes))
            if len(end_nodes) > 1:
                if len(end_nodes) % 2 == 1:
                    print(len(end_nodes)//2)
                    for k in range(len(end_nodes)//2):
                        print(end_nodes[0:1])
                        losers.append(end_nodes[0:1])
                        cur_lose.append(end_nodes[0:1])
                        end_nodes.remove(end_nodes[0:1])
            print(cur_lose)

        for i in cur_lose:
            print(i)
            list.remove(list[i])

    run_connects(elements)
    return losers





if __name__ == '__main__':

    n = int(input().strip())

    elements = map(int, input().rstrip().split())

    print(nuclearFusion(elements))

#
# def is_end(list, n):
#     for i in range(len(list)):
#         if n == list[i]:
#             return False
#         else:
#             pass
#     return True
# for i in range(8):
#
#     print(is_end([1, 1, 1, 2, 2, 4, 4, 4], i + 2))