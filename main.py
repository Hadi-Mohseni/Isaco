from models import Product
from PyQt5 import QtWidgets
import sys
from typing import List
from PyQt5.QtCore import Qt
import asyncio


class MainForm(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.top_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)
        self.initialize_table()
        self.initialize_bottom_bar()

    def initialize_table(self):
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        headers = [
            "شرح",
            "بارکد",
            "قیمت فروشگاه",
            "قیمت شرکت",
            "وضعیت",
            "موجودی",
            "بروزرسانی؟",
        ]
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setLayoutDirection(Qt.RightToLeft)
        self.top_layout.addWidget(self.table)
        self.table.setColumnWidth(0, 500)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 150)
        self.table.setSortingEnabled(True)

    def set_products(self, products=List[Product]):
        self.products = products
        self.checkboxes = []

        for row, product in enumerate(products):
            self.table.insertRow(row)
            description = QtWidgets.QTableWidgetItem(str(product.description))
            barcode = QtWidgets.QTableWidgetItem(str(product.barcode))
            price = QtWidgets.QTableWidgetItem(str(product.price))
            company_price = QtWidgets.QTableWidgetItem(str(product.company_price))
            status = QtWidgets.QTableWidgetItem(str(product.status))
            quantity = QtWidgets.QTableWidgetItem(str(product.quantity))
            check_box = QtWidgets.QCheckBox()
            check_box.setChecked(False)
            check_box.stateChanged.connect(product.on_checkbox_changed)

            # Set columns to fill the table horizontally
            self.table.setItem(row, 0, description)
            self.table.setItem(row, 1, barcode)
            self.table.setItem(row, 2, price)
            self.table.setItem(row, 3, company_price)
            self.table.setItem(row, 4, status)
            self.table.setItem(row, 5, quantity)
            self.table.setCellWidget(row, 6, check_box)

    def initialize_bottom_bar(self):
        self.btn_update = QtWidgets.QPushButton("بروزرسانی")
        self.btn_start = QtWidgets.QPushButton("شروع")

        # Left side widgets
        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(self.btn_update)

        # Right side widgets
        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addWidget(self.btn_start)

        # Add left and right layouts to bottom layout
        self.bottom_layout.addLayout(left_layout)
        self.bottom_layout.addLayout(right_layout)

        self.btn_start.clicked.connect(self.start)
        self.btn_update.clicked.connect(self.update_prices)

    def start(self):
        excel_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            windows,
            "Open File",
            "",
            "Excel Files (*.xlsx)",
        )

        if excel_path:
            products = Product.list_all(excel_path)
            self.set_products(products)

    def update_prices(self):
        for product in self.products:
            if product.update == True:
                product.update_price()

        QtWidgets.QMessageBox.information(
            self,
            "عملیات موفق",
            "قیمت ها با موفقیت بروزرسانی شدند!",
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok,
        )

        self.table.clearContents()
        self.products = []


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = MainForm()
    windows.resize(500, 500)
    windows.move(100, 100)
    windows.show()
    text = QtWidgets.QLineEdit()
    sys.exit(app.exec_())
