"""
The flask application package.
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

import AgileStockWeb.views
from AgileStockWeb.models.out_formatter import logger
from AgileStockWeb.database import Database


#app.config is a hash variable needed for a connection string
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '4LocalDB'
app.config['MYSQL_DB'] = 'agilestockinv'


logger.info(f"Initializing database")
db = Database(app)
logger.info(f"Database created")


from AgileStockWeb.models.book import Book

wolfBook = Book(
    "The Wolves of Winter",
    "Tyrell Johnson",
    "Scribner",
    "2018",
    "Action",
    "9781501155680"
)

db.insert_intoBOOK(wolfBook.title, wolfBook.author, wolfBook.publisher, wolfBook.publishedDate, wolfBook.genre, wolfBook.isbn)

