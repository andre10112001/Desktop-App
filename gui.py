import tkinter as tk
from PIL import Image, ImageTk

def get_input_text(data_list):
    input_text = entry.get()
    data_list.append(input_text)
    print(data_list)
    entry.delete(0, "end")

data = []
window = tk.Tk()
window.title(" Body measurements tracker ")
window.geometry("600x400")

frame_ex = tk.Frame(window, borderwidth=2, relief="ridge")
frame_ex.grid(row=0, column=0)  # Adjust padx and pady as needed

# Add widgets to the frame (e.g., labels, buttons)
label = tk.Label(frame_ex, text="This is a frame!")
label.pack()

entry = tk.Entry(frame_ex)
entry.pack()

button = tk.Button(frame_ex, text="Get Text", command=lambda: get_input_text(data))
button.pack()

frame_ex = tk.Frame(window, borderwidth=2, relief="ridge")
frame_ex.grid(row=1, column=0)  # Adjust padx and pady as needed

# Add widgets to the frame (e.g., labels, buttons)
label = tk.Label(frame_ex, text="This is a frame!")
label.pack()

button = tk.Button(frame_ex, text="Click Me 2")
button.pack()

image = Image.open("Body.png")  # Replace with the image file's name
img = ImageTk.PhotoImage(image)
label = tk.Label(window, image=img)
label.grid(row=0, column=1, rowspan=2)




window.mainloop()