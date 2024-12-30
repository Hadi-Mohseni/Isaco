from tkinter import *
from tkinter import ttk
from awesometkinter.bidirender import render_text as _
from models import Product


class Row(ttk.Frame):

    def __init__(self, master=None, product: Product = {}):
        super().__init__(master, relief="solid", height=200, width=500)
        self.product = product

        description = ttk.Label(
            self,
            text=_(product.description),
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=100,
        )
        barcode = ttk.Label(
            self,
            text=product.barcode,
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=50,
        )
        price = ttk.Label(
            self,
            text=product.price,
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=50,
        )
        company_price = ttk.Label(
            self,
            text=product.company_price,
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=50,
        )
        status = ttk.Label(
            self,
            text=_(product.status),
            background="white",
            relief="solid",
            anchor="e",
            padding=5,
            width=50,
        )

        self.update = BooleanVar()
        check = ttk.Checkbutton(
            self,
            text=_("بروزرسانی"),
            onvalue=True,
            offvalue=False,
            variable=self.update,
            width=50,
        )

        description.grid(row=0, column=5, sticky=(W, E))
        barcode.grid(row=0, column=4, sticky=(W, E))
        price.grid(row=0, column=3, sticky=(W, E))
        company_price.grid(row=0, column=2, sticky=(W, E))
        status.grid(row=0, column=1, sticky=(W, E))
        check.grid(row=0, column=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
