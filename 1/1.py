import tkinter as tk
import csv

incomingData = dict([{"year1, prod1","100uah"},
                     {"year1, prod2","100uah"},
                     {"year1, prod3","100uah"},
                     {"year1, prod4","100uah"},
                     {"year1, prod5","100uah"},
                     {"year1, prod6","100uah"},
                     {"year1, prod7","100uah"},
                     {"year1, prod8","100uah"},
                     {"year1, prod9","100uah"},
                     {"year1, prod10","100uah"},
                     {"year2, prod1","100uah"},
                     {"year2, prod2","100uah"},
                     {"year2, prod3","100uah"},
                     {"year2, prod4","100uah"},
                     {"year2, prod5","100uah"},
                     {"year2, prod6","100uah"},
                     {"year2, prod7","100uah"},
                     {"year2, prod8","100uah"},
                     {"year2, prod9","100uah"},
                     {"year2, prod10","100uah"},
                     {"year3, prod1","100uah"},
                     {"year3, prod2","100uah"},
                     {"year3, prod3","100uah"},
                     {"year3, prod4","100uah"},
                     {"year3, prod5","100uah"},
                     {"year3, prod6","100uah"},
                     {"year3, prod7","100uah"},
                     {"year3, prod8","100uah"},
                     {"year3, prod9","100uah"},
                     {"year3, prod10","100uah"}])

def writeToFile():
    with open("1/result.csv", "w") as f:
        writer = csv.writer(f)
        for key, value in incomingData.items():
             writer.writerow([key, value])

m = tk.Tk()
m.title("")
m.configure(width=220, height=180, bg="sky blue")

button = tk.Button(m, text="Записати", command=writeToFile)
button.place(x=110, y=90)

m.mainloop()
