import tkinter as tk
from tkinter import *
from tkinter import colorchooser

import math

# Color picking function
def choose_color():
    color_code = colorchooser.askcolor(title="Selecting color...")
    print(color_code)
    #return color_code

# Coordinates and selected color
def on_mouse_drag(event):
    x = event.x
    y = event.y
    #x = 1
    #y = 320

    canvas_height = 642
    canvas_width = 642
    inverted_x = canvas_width - x
    inverted_y = canvas_height - y

    print("X is {}, Y is {} ; invX is {}, invY is {}".format(x, y, inverted_x, inverted_y))
    
    canvas.delete("all")
    canvas.create_image(320, 320, image=wheel)
    canvas.create_image(x, y, image=target)
    canvas.create_image(inverted_x, inverted_y, image=target)

    rgb_color = wheel.get(x, y)
    hex_color = "#{:02x}{:02x}{:02x}".format(*rgb_color)

    color_label.set(hex_color + "\nrgb({},{},{})".format(*rgb_color))
    color_select['bg'] = hex_color


# Root window
root = Tk()
root.title("TomatoFLUX")

#button = Button(root, text = "Select color", command = choose_color)
#button.pack()
canvas = tk.Canvas(root, height=720 , width=720)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
canvas.bind("<B1-Motion>", on_mouse_drag)

color_label = tk.StringVar()
color_label.set('#FFFFFF\nrgb(255,255,255)')
color_select = tk.Label(root, textvariable=color_label, bg='white', width=20, font=('Arial', 20, 'bold'))
color_select.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

wheel = tk.PhotoImage(file='./wheel.png')
target = tk.PhotoImage(file='./target.png')

root.geometry("1280x720")
root.mainloop()