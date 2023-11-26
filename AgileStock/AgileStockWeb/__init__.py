"""
The flask application package.
"""

#Before running, ensure Python 3.11 is installed.
#A command can be run to begin the development server
#    cd .\pywebtwo
#    py -m runserver
#
#
# OUTPUT:
#    PS C:\Dev\python\PythonWebTESTFlaskWebProject1\pywebtwo> py -m runserver
#     * Serving Flask app 'FlaskWebProject1'
#     * Debug mode: off
#    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#     * Running on http://localhost:7000
#    Press CTRL+C to quit


from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

import AgileStockWeb.views

# from datetime import datetime

#  # import Inventory class
# #from AgileStockWeb.models import Inventory

#  #import SQL
# import os
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func

# #SQL
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'mysql:///root:ALT4c352@localhost:3306/agilestockinv'
# app.config['SQLALCHEMNY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# #an inventory object
# #keyBoard = Inventory.Inventory("Keyboard", 0)
# #print(f"name:{keyBoard.name:s}, itemNum:{keyBoard.itemNum}")
# #an inventory object end

