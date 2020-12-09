import tkinter as tk
import os 
from tkinter import filedialog, Text 

root = tk.Tk()

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split('',) 
        apps = [x for x in tempApps if x.strip()]

def addAppToOpen():
    for widget in frame.winfo_children:
        widget.destroy()
    
    fileName = filedialog.askopenfilename(initialdir = "/", title = "Select File", 
                                          filetypes = (("executables", "*.exe"), ("allfiles", "*.*")))
    apps.append(fileName)
    print(fileName)
    for app in apps:
        label = tk.Label(frame, text = app, fg = "black")
        label.pack();
        
def runApps():
    for app in apps:
        os.startfile(app)
    

canvas = tk.Canvas(root, height = 700, width = 700, bg = "#51168c" ) 
canvas.pack()

frame = tk.Frame(root, bg = "#7a50a3")
frame.place(relwidth  = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text = "Open File", padx = 10, pady = 5, fg = "black", command = addAppToOpen)
openFile.pack()

runApps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg = "black", command = runApps)
runApps.pack()

for app in apps :
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps :
        f.write(app + ',')
    