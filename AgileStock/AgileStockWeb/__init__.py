"""
The flask application package.
"""

#Application start
#Connexion API + Flask application
import connexion
app = connexion.FlaskApp(__name__.split('.')[0])
app.add_api("../swagger.yml")
app = app.app


#from AgileStockWeb.models.out_formatter import logger
from AgileStockWeb.database import CreateDatabase
from AgileStockWeb.people import read_all
print(read_all)

#app.config is a hash variable needed for a connection string
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '4LocalDB'
app.config['MYSQL_DB'] = 'agilestockinv'
db = CreateDatabase(app)




from AgileStockWeb.models.inventory import Book, AS_Item
wolfBook = Book(
    "The Wolves of Winter",
    "Tyrell Johnson",
    "Scribner",
    "2018",
    "Action",
    "9781501155680"
)

APIexampleitem_InventoryFromScannerApp = AS_Item(12345, "bookofsomesort", "action", "5432112345ABCD")
#db.insert_intoBOOK(wolfBook.title, wolfBook.author, wolfBook.publisher, wolfBook.publishedDate, wolfBook.genre, wolfBook.isbn)
db.insert_intoAS_ITEM(APIexampleitem_InventoryFromScannerApp.barcode,
    APIexampleitem_InventoryFromScannerApp.productName,
    APIexampleitem_InventoryFromScannerApp.productCategory,
    APIexampleitem_InventoryFromScannerApp.inventorySKU)
AS_ITEMresult = db.fetch_fromAS_ITEM()
APIexampleitem2_InventoryFromScannerApp = AS_Item(5555, "booktwo", "action", "543BCD")
#db.insert_intoBOOK(wolfBook.title, wolfBook.author, wolfBook.publisher, wolfBook.publishedDate, wolfBook.genre, wolfBook.isbn)
db.insert_intoAS_ITEM(APIexampleitem2_InventoryFromScannerApp.barcode,
    APIexampleitem2_InventoryFromScannerApp.productName,
    APIexampleitem2_InventoryFromScannerApp.productCategory,
    APIexampleitem2_InventoryFromScannerApp.inventorySKU)
AS_ITEM2result = db.fetch_fromAS_ITEM()
APIexampleitem3_InventoryFromScannerApp = AS_Item(84527, "third book", "action/comedy", "ID#5432112345ABCD")
#db.insert_intoBOOK(wolfBook.title, wolfBook.author, wolfBook.publisher, wolfBook.publishedDate, wolfBook.genre, wolfBook.isbn)
db.insert_intoAS_ITEM(APIexampleitem3_InventoryFromScannerApp.barcode,
    APIexampleitem3_InventoryFromScannerApp.productName,
    APIexampleitem3_InventoryFromScannerApp.productCategory,
    APIexampleitem3_InventoryFromScannerApp.inventorySKU)
AS_ITEM3result = db.fetch_fromAS_ITEM()