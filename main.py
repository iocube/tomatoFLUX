import tkinter as tk
from tkinter import *
from tkinter import colorchooser

import math


# Menu at the bottom 
# Giant circle to the left
# Color pick palette to the right

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

    padding = 20
    canvas_height = 720 + padding
    canvas_width = 720 + padding
    inverted_x = canvas_width - x + padding
    inverted_y = canvas_height - y + padding

    print("X is {}, Y is {} ; invX is {}, invY is {}".format(x, y, inverted_x, inverted_y))
    
    canvas.delete("all")

    # Color wheel
    canvas.create_image(20, 20, image=wheel, anchor=NW)
    # Crosshair 1
    canvas.create_image(x, y, image=target)
    # Crosshair 2
    canvas.create_image(inverted_x, inverted_y, image=target)

    # Selected colors
    rgb_color = wheel.get(x - 20, y - 20)
    hex_color = "#{:02x}{:02x}{:02x}".format(*rgb_color)

    color_label.set(hex_color + "\nrgb({},{},{})".format(*rgb_color))
    color_select['bg'] = hex_color


# Root window
root = Tk()
root.title("TomatoFLUX")

#button = Button(root, text = "Select color", command = choose_color)
#button.pack()

canvas = tk.Canvas(root, height=760 , width=760)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
canvas.bind("<B1-Motion>", on_mouse_drag)

color_label = tk.StringVar()
color_label.set('#FFFFFF\nrgb(255,255,255)')
color_select = tk.Label(root, textvariable=color_label, bg='white', width=20, font=('Arial', 20, 'bold'))
color_select.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

# old small
#wheel = tk.PhotoImage(file='./wheel.png')
# big 
wheel = tk.PhotoImage(file='./color_wheel.png')

calculate_adjust = 720 - wheel.height()
print(calculate_adjust)
#wheel = tk.PhotoImage(data=bytes(colour_wheel()))
target = tk.PhotoImage(file='./target.png')

root.geometry("1280x760")
root.mainloop()