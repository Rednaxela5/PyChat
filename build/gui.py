from pathlib import Path
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox, font
from default_entry import DefaultTextEntry
import tkinter as tk


# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x568")
window.configure(bg = "#0F2634")
window.title("PyChat")

fontstyle = "Montserrat"

d_chat_entry = "Write a message..."
d_search_entry = "Search"
canvas = Canvas(
    window,
    bg = "#0F2634",
    height = 568,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    252.0,
    0.0,
    1024.0,
    568.0,
    fill="#CCD3D8",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    activebackground="#ccd3d8",
    cursor='hand2',
    relief="flat"
)
button_1.place(
    x=968.0,
    y=516.0,
    width=56.0,
    height=52.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    610.0,
    542.0,
    image=entry_image_1
)
entry_1 = DefaultTextEntry(
    bd=0,
    bg="#FFFFFF",
    default_text=d_chat_entry,
    font=fontstyle,
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=265.0,
    y=516.0,
    width=716.0,
    height=50.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    143.0,
    29.0,
    image=entry_image_2
)
entry_2 = DefaultTextEntry(
    bd=0,
    bg="#E7E7E7",
    font=fontstyle,
    default_text=d_search_entry,
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=50.0,
    y=12.0,
    width=175.0,
    height=32.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    29.0,
    29.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    activebackground="#0f2634",
    cursor='hand2',
    relief="flat"
)
button_2.place(
    x=4.0,
    y=516.0,
    width=244.0,
    height=47.0
)

button_image_hover_2 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

def button_2_hover(e):
    button_2.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    button_2.config(
        image=button_image_2
    )

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    activebackground="#0f2634",
    cursor='hand2',
    relief="flat"
)
button_3.place(
    x=4.0,
    y=118.0,
    width=244.0,
    height=54.0
)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

def button_3_hover(e):
    button_3.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    button_3.config(
        image=button_image_3
    )

button_3.bind('<Enter>', button_3_hover)
button_3.bind('<Leave>', button_3_leave)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    activebackground="#0f2634",
    cursor='hand2',
    relief="flat"
)
button_4.place(
    x=4.0,
    y=64.0,
    width=244.0,
    height=54.0
)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_3.png"))

def button_4_hover(e):
    button_4.config(
        image=button_image_hover_4
    )
def button_4_leave(e):
    button_4.config(
        image=button_image_4
    )

button_4.bind('<Enter>', button_4_hover)
button_4.bind('<Leave>', button_4_leave)


image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    638.0,
    29.0,
    image=image_image_2
)

canvas.create_text(
    270.0,
    16.0,
    anchor="nw",
    text="Juan Dela Cruz",
    fill="#0F2634",
    font=("Montserrat", 13, "bold")
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    activebackground="#c0c5c8",
    cursor='hand2',
    relief="flat"
)
button_5.place(
    x=968.0,
    y=12.0,
    width=36.0,
    height=36.0
)

button_image_hover_5 = PhotoImage(
    file=relative_to_assets("button_hover_4.png"))

def button_5_hover(e):
    button_5.config(
        image=button_image_hover_5
    )
def button_5_leave(e):
    button_5.config(
        image=button_image_5
    )

button_5.bind('<Enter>', button_5_hover)
button_5.bind('<Leave>', button_5_leave)


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    412.0,
    100.0,
    image=image_image_3
)

canvas.create_text(
    335.0,
    92.0,
    anchor="nw",
    text="anong balita, sa radyo at TV?",
    fill="#2C2828",
    font=("Montserrat", 14 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    866.0,
    157.0,
    image=image_image_4
)

canvas.create_text(
    751.0,
    148.0,
    anchor="nw",
    text="gano'n pa rin, kumakapa sa dilim",
    fill="#FFFFFF",
    font=("Montserrat", 14 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    450.0,
    214.0,
    image=image_image_5
)

canvas.create_text(
    335.0,
    206.0,
    anchor="nw",
    text="minsa'y naisip ko na umalis na lang dito",
    fill="#2C2828",
    font=("Montserrat", 14 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    847.0,
    271.0,
    image=image_image_6
)

canvas.create_text(
    712.0,
    263.0,
    anchor="nw",
    text="kalimutan ang lahat, lumipad, lumayo?",
    fill="#FFFFFF",
    font=("Montserrat", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
