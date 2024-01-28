"""
The flask application package.
"""

import os
from flask import Flask, request, jsonify

app = Flask(__name__)


# from AgileStockWeb.models.out_formatter import logger
from AgileStockWeb.database.db import CreateDatabase

if not os.environ.get("AZURE_ENVIRONMENT") == "AZUREPROD":
    # These (commented) credentials were used for local MySQL database connection string
    # #app.config is a hash variable needed for a connection string
    app.config["MYSQL_HOST"] = "127.0.0.1"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "4LocalDB"
    app.config["MYSQL_DB"] = "agilestockinv"
else:
    # The below (4) app config variables are used only in azure deployed environment
    app.config["MYSQL_HOST"] = os.environ.get("AZURE_MYSQL_HOST")
    app.config["MYSQL_USER"] = os.environ.get("AZURE_MYSQL_USER")
    app.config["MYSQL_PASSWORD"] = os.environ.get("AZURE_MYSQL_PASSWORD")
    app.config["MYSQL_DB"] = os.environ.get("AZURE_MYSQL_NAME")

db = CreateDatabase(app)

from AgileStockWeb.models.book import AS_BOOK

APIexampleitem_InventoryFromScannerApp = AS_BOOK(
    "TheActualBook",
    "Books author",
    "action books",
    "5432112345ABCD",
    "Comedy",
    "1234567890",
)
db.insert_intoAS_BOOK(
    APIexampleitem_InventoryFromScannerApp.isbn,
    APIexampleitem_InventoryFromScannerApp.title,
    APIexampleitem_InventoryFromScannerApp.author,
    APIexampleitem_InventoryFromScannerApp.publisher,
    APIexampleitem_InventoryFromScannerApp.publishedDate,
    APIexampleitem_InventoryFromScannerApp.genre,
)


from AgileStockWeb import views
