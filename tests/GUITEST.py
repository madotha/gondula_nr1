# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:27:42 2018

@author: Stef
"""

import tkinter as tk

counter = 0


def counter_label(label, label2):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label2.config(text=str(counter+10))
        label.after(1000, count)

    count()



root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Counting Seconds")
label = tk.Label(root, text="error", fg="green")
label.pack()
label.columnconfigure(0, weight=1)
test = tk.Label(root, text="test", fg="green")
test.pack_configure()
tk.R
counter_label(label, test)



# counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()