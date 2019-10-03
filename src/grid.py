#!/usr/bin/env python3
# coding: utf-8
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
tree = ttk.Treeview(root)
tree["columns"] = (1,2,3)
tree["show"] = "headings"
#tree.column(1,width=75)
#tree.column(2,width=75)
#tree.column(3,width=100)
tree.column(1)
tree.column(2)
tree.column(3)
tree.heading(1,text="識別子")
tree.heading(2,text="名前")
tree.heading(3,text="生年月日")
tree.grid(sticky="SNEW") # これがあってもリサイズ対応してくれない
tree.insert("","end",values=(1,"山田太郎","1950-01-01"))
tree.insert("","end",values=(2,"鈴木二郎","1960-02-02"))
tree.insert("","end",values=(3,"川村三郎","1970-03-03"))
tree.pack()
root.mainloop()

