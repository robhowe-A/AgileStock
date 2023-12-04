"""
The flask application package.
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

import AgileStockWeb.views
from AgileStockWeb.models.out_formatter import logging, CustomFormatter, logger
from AgileStockWeb.database import Database


#app.config is a hash variable needed for a connection string
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '4LocalDB'
app.config['MYSQL_DB'] = 'agilestockinv'


logger.info(f"Initializing database")
db = Database(app)
logger.info(f"Database created")