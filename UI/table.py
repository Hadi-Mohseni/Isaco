from tkinter import ttk
from tkinter import *
from typing import List
from models import Product
from UI import Row
from awesometkinter.bidirender import render_text as _
from customtkinter import CTkScrollableFrame
from tkinter import messagebox


class Header(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master, relief="solid", height=200, width=500)
        description = ttk.Label(
            self,
            text=_("شرح"),
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=100,
        )
        barcode = ttk.Label(
            self,
            text=_("کدکالا"),
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=50,
        )
        price = ttk.Label(
            self,
            text=_("قیمت فروشگاه"),
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=50,
        )
        company_price = ttk.Label(
            self,
            text=_("قیمت شرکت"),
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=50,
        )
        status = ttk.Label(
            self,
            text=_("افزایش"),
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=50,
        )

        check = ttk.Label(
            self,
            text=_(""),
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=50,
        )

        description.grid(row=0, column=5, sticky=(W, E))
        barcode.grid(row=0, column=4, sticky=(W, E))
        price.grid(row=0, column=3, sticky=(W, E))
        company_price.grid(row=0, column=2, sticky=(W, E))
        status.grid(row=0, column=1, sticky=(W, E))
        check.grid(row=0, column=0, sticky=(W, E))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)


class Table(CTkScrollableFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        header = Header(self)
        header.grid(row=0, column=0, sticky=(W, E))
        self.columnconfigure(0, weight=1)

    def set(self, products: List[Product]):
        self.rows = []
        for index, product in enumerate(products):
            if product.price == product.company_price:
                continue
            row = Row(self, product)
            row.grid(row=index + 1, column=0, sticky=(W, E))
            self.rows.append(row)

    def update_price(self):
        for row in self.rows:
            if row.update.get():
                row.product.update()
        messagebox.showinfo("ok", _("عملیات با موفقیت انجام شد!"))
        self.rows = []
        for child in self.winfo_children():
            child.destroy()
