from awesometkinter.bidirender import render_text as _
from models import Product
from tkinter import *
from tkinter import messagebox
import customtkinter
from UI import Table


def load_products():
    products = Product.list_all()
    table.set(products)


def update_price():
    if messagebox.askyesno("Message", _("آیا مطمئن به بروزرسانی هستید؟")):
        table.update_price()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("دستیار ایساکو")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# --------------- Main Frame
# ---------------

mainframe = customtkinter.CTkFrame(root, width=500, height=700)
table = Table(mainframe, width=500, height=500)

mainframe.grid(row=0, column=0, sticky=NSEW)
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
table.grid(row=0, column=0, sticky=NSEW)

# --------------- Bottom Frame
# ---------------
b_frame = customtkinter.CTkFrame(root, width=200, height=50)
bl_frame = customtkinter.CTkFrame(b_frame, width=200, height=100)
br_frame = customtkinter.CTkFrame(b_frame, width=200, height=100)

btn_start = customtkinter.CTkButton(
    br_frame,
    text=_("شروع"),
    command=load_products,
    height=100,
)

btn_update = customtkinter.CTkButton(
    bl_frame,
    text=_("بروزرسانی"),
    command=update_price,
    height=100,
    fg_color="white",
    text_color="black",
)

b_frame.grid(row=1, column=0, sticky=(N, E, W))
bl_frame.grid(row=0, column=0, sticky=NSEW)
br_frame.grid(row=0, column=1, sticky=NSEW)
btn_start.grid(row=0, column=0, sticky=NSEW)
btn_update.grid(row=0, column=0, sticky=NSEW)
b_frame.columnconfigure(0, weight=1)


root.mainloop()
