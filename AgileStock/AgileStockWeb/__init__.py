"""
The flask application package.
"""
from flask import Flask, request, jsonify

app = Flask(__name__)


#from AgileStockWeb.models.out_formatter import logger
from AgileStockWeb.database.db import CreateDatabase



#app.config is a hash variable needed for a connection string
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '4LocalDB'
app.config['MYSQL_DB'] = 'agilestockinv'


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