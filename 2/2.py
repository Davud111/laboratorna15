import tkinter as tk
import re

def handlePunctuatation(text):
    return re.sub(r'[!"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]', "", text)

m = tk.Tk()
m.title = ""
m.geometry("250x150")

entry = tk.Entry(m)
entry.grid(row=0, column=0, padx=5, pady=5)

label = tk.Label(m)
label.grid(row=2, column=0, padx=5, pady=5)

button = tk.Button(m, text="Видалити усі службові символи", command=lambda : label.configure(text=handlePunctuatation(entry.get())))
button.grid(row=1, column=0, padx=5, pady=5)

m.mainloop()
