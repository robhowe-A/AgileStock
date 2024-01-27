class AS_BOOK:
    def __init__(self, title, author, publisher, publishedDate, genre, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publishedDate = publishedDate
        self.genre = genre
        self.isbn = isbn


class User:
    def __init__(self, email, password, f_Name, l_Name):
        self.email = email
        self.password = password
        self.f_Name = f_Name
        self.l_Name = l_Name


class Inventory:
    def __init__(self, serialnumber, quantity, date_RX):
        self.serialnumber = serialnumber
        self.quantity = quantity
        self.date_RX = date_RX


class AS_Item:
    def __init__(self, barcode, productName, productCategory, intenvorySKU):
        self.barcode = barcode
        self.productName = productName
        self.productCategory = productCategory
        self.inventorySKU = intenvorySKU
