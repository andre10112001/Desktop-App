import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def get_entry_data(event):
    entry_text = text1.get() 
    text1.delete(0, "end")  
    print(entry_text)


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
text1.bind("<Return>", get_entry_data)

# Adding a submit button
extract_button = ttk.Button(frame1, text="Extract Data", command=lambda: get_entry_data(event=None), bootstyle=SUCCESS)
extract_button.place(x=220,y=50, width=130)

root.mainloop()