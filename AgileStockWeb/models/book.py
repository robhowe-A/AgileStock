##########################################################################
## Company: AgileStock
## Engineer(s): Robert Howell
##
## Create Date:    12/3/2023
## Project Name:    AgileStock
## Target Devices:    Web
## Tool versions:    Python 3.11
## Description:   Project Models
## Dependencies:
##   -module(s):
##
##   -packages(s):
##      blinker==1.7.0
##      click==8.1.7
##      colorama==0.4.6
##      Flask==3.0.0
##      itsdangerous==2.1.2
##      Jinja2==3.1.2
##      MarkupSafe==2.1.3
##      PyMySQL==1.1.0
##      Werkzeug==3.0.1
##
## Revision: 1.0 - File Created
## Additional Comments: AS_BOOK class defined for database, web server
##
##########################################################################


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
