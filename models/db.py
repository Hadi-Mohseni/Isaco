import pyodbc
import dotenv


class Database:

    @staticmethod
    def list_all_products():
        connection_string = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=192.168.2.200\SQL2019;DATABASE=KhodroIsaco;UID=sa;PWD=6626;TrustServerCertificate=YES"
        cnxn = pyodbc.connect(connection_string)
        cursor = cnxn.cursor()
        cursor.execute(
            " select Kala.shrh, Kala.CodKala, KalaGimat.Gimat, MojodiKala_View.Mojodi  from KalaGimat inner join Kala on Kala.CodKala=KalaGimat.CodKala inner join MojodiKala_View on kala.CodKala = MojodiKala_View.CodKala where Kala.shrh like '%ساکو%' and MojodiKala_View.SalMali = 1404"
        )
        result = cursor.fetchall()
        return result

    @staticmethod
    def update_product_price(barcode: str, price: str):
        connection_string = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=192.168.2.200\SQL2019;DATABASE=KhodroIsaco;UID=sa;PWD=6626;TrustServerCertificate=YES"
        cnxn = pyodbc.connect(connection_string)
        cursor = cnxn.cursor()
        cursor.execute(f"update KalaGimat set Gimat={price} where CodKala='{barcode}'")
        cursor.commit()
