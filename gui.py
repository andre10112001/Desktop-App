import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def get_entry_data(entrys, data):
    body_parts = ["Biceps", "Legs", "Chest"]
    for i, entry in enumerate(entrys):
        entry_text = entry.get() 
        entry.delete(0, "end")  
        data[body_parts[i]] = entry_text
    print(data)
    return data

entrys_list = []
data = {}
# Initializing the window
root = ttk.Window(themename="darkly")
root.geometry("500x500")
root.title("Body Measurments Tracker")

frame1 = ttk.Frame()
frame1.place(x=0, y=0, width=350, height=100)
# Adding a label
label1 = ttk.Label(frame1, text="Biceps:", bootstyle="succes")
label1.place(x=0, y=0)

# Adding data entry 
text1 = ttk.Entry(frame1,bootstyle="success")
text1.insert(0, "40 cm")
text1.place(x=0, y=50, width=200)
entrys_list.append(text1)

frame2 = ttk.Frame()
frame2.place(x=0, y=100, width=350, height=100)
# Adding a label
label2 = ttk.Label(frame2, text="Legs:", bootstyle="succes")
label2.place(x=0, y=0)

# Adding data entry 
text2 = ttk.Entry(frame2,bootstyle="success")
text2.insert(0, "40 cm")
text2.place(x=0, y=50, width=200)
entrys_list.append(text2)

frame3 = ttk.Frame()
frame3.place(x=0, y=200, width=350, height=100)
# Adding a label
label3 = ttk.Label(frame3, text="Legs:", bootstyle="succes")
label3.place(x=0, y=0)

# Adding data entry 
text3 = ttk.Entry(frame3,bootstyle="success")
text3.insert(0, "40 cm")
text3.place(x=0, y=50, width=200)
entrys_list.append(text3)

# Adding a submit button
extract_button = ttk.Button(root, text="Extract Data", command=lambda: get_entry_data(entrys_list, data), bootstyle=SUCCESS)
extract_button.place(x=220,y=400, width=130)

root.mainloop()