import tkinter as tk
import random

def move_button(event):
    button.place(x=random.randint(0, window_width-100), y=random.randint(0, window_height-50))

def create_window():
    global window_width, window_height, button

    window = tk.Tk()
    window_width = 600
    window_height = 600

    window.geometry(f"{window_width}x{window_height}")

    button = tk.Button(window, text="Quer namorar comigo? clique aqui")
    button.place(x=window_width/2-100, y=window_height/2-25)
    button.bind("<Enter>", move_button)

    window.mainloop()

create_window()