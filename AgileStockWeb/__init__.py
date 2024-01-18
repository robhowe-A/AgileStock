"""
The flask application package.
"""
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


#from AgileStockWeb.models.out_formatter import logger
from AgileStockWeb.database.db import CreateDatabase
if not os.environ.get("AZURE_ENVIRONMENT") == "AZUREPROD":
    # These (commented) credentials were used for local MySQL database connection string
    # #app.config is a hash variable needed for a connection string
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '4LocalDB'
    app.config['MYSQL_DB'] = 'agilestockinv'
else:
    #The below (4) app config variables are used only in azure deployed environment
    app.config['MYSQL_HOST'] = os.environ.get("AZURE_MYSQL_HOST")
    app.config['MYSQL_USER'] = os.environ.get("AZURE_MYSQL_USER")
    app.config['MYSQL_PASSWORD'] = os.environ.get("AZURE_MYSQL_PASSWORD")
    app.config['MYSQL_DB'] = os.environ.get("AZURE_MYSQL_NAME")


db = CreateDatabase(app)


from AgileStockWeb.models.book import Book, AS_Item

wolfBook = Book(
    "The Wolves of Winter",
    "Tyrell Johnson",
    "Scribner",
    "2018",
    "Action",
    "9781501155680"
)

APIexampleitem_InventoryFromScannerApp = AS_Item(12345, "bookofsomesort", "action", "5432112345ABCD")
db.insert_intoAS_ITEM(APIexampleitem_InventoryFromScannerApp.barcode,
    APIexampleitem_InventoryFromScannerApp.productName,
    APIexampleitem_InventoryFromScannerApp.productCategory,
    APIexampleitem_InventoryFromScannerApp.inventorySKU)


from AgileStockWeb import views