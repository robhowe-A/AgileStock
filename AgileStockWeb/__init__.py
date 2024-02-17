##########################################################################
## Company: AgileStock
## Engineer(s): Robert Howell, Branson Addington
## 
## Create Date:    12/3/2023
## Project Name:    AgileStock
## Target Devices:    Web
## Tool versions:    Python 3.11
## Description:   Project initialization, database creation, and database seed.
## Dependencies:
##   -module(s):
##      os
##      flask
##      AgileStockWeb.database.db
##      AgileStockWeb.models.book
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
## Revision: 1.1 - Environment if-else statement, for Azure deployment
## Revision: 1.0 - File Created
## Additional Comments: Python CRUD operations run here as dev operations, adding
##  books before website runtime begins.
##
##########################################################################

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

# db.delete_AS_BOOK("pymysql changes", 1)

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
db.insert_intoAS_BOOK(12345, "ASBOOK1","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
db.insert_intoAS_BOOK(123456, "ASBOOK2","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
db.insert_intoAS_BOOK(123457, "ASBOOK3","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
db.insert_intoAS_BOOK(123458, "ASBOOK4","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
db.insert_intoAS_BOOK(123459, "ASBOOK5","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
db.insert_intoAS_BOOK(123450, "ASBOOK6","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
db.insert_intoAS_BOOK(1234511, "ASBOOK7","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
db.insert_intoAS_BOOK(1234512, "ASBOOK8","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
db.insert_intoAS_BOOK(1234513, "ASBOOK9","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
db.insert_intoAS_BOOK(1234514, "ASBOOK10","TEAM_ALPHA", "CSC480C", 2024, "NONFICTION")
# from AgileStockWeb import views
