from flask import Flask, render_template, request, url_for, redirect
from AgileStockWeb import app

import AgileStockWeb.views

from datetime import datetime

 # import Inventory class
#from AgileStockWeb.models import Inventory

 #import SQL
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

#SQL
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql:///root:ALT4c352@localhost:3306/agilestockinv'
app.config['SQLALCHEMNY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#an inventory object
#keyBoard = Inventory.Inventory("Keyboard", 0)
#print(f"name:{keyBoard.name:s}, itemNum:{keyBoard.itemNum}")
#an inventory object end

