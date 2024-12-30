from joblib import Parallel, delayed
from tkinter import filedialog
from .db import Database
import pandas


class Product:

    def __init__(
        self,
        description: str,
        barcode: str,
        price: int,
        company_price: int,
    ):
        self.description = description
        self.barcode = barcode
        self.price = int(price)
        self.company_price = int(company_price) + (10000 - int(company_price) % 10000)
        self.status = "افزایش" if self.company_price > self.price else "کاهش"

    @staticmethod
    def list_all():
        filename = filedialog.askopenfile(filetypes=(("Excel file", "*.xlsx"),))

        def compare(product, isaco_products):
            for ip in isaco_products:
                if product[1] == ip[1]:
                    return Product(product[0], product[1], product[2], ip[2])

        excel = pandas.read_excel(filename.name, dtype=str).to_numpy()
        isaco_products = []
        for row in excel:
            isaco_products.append([row[1], row[0], row[6]])
        shop_products = Database.list_all_products()[:50]
        shop_products = [[x[0], x[1].replace(" ", ""), x[2]] for x in shop_products]

        result = Parallel(n_jobs=-1)(
            delayed(compare)(i, isaco_products) for i in shop_products
        )

        return result

    def update(self):
        Database.update_product_price(self.barcode, self.company_price)
