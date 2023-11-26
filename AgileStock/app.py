from flask import Flask, render_template, request, url_for, redirect
from AgileStockWeb import app

import AgileStockWeb.views

from datetime import datetime

 # import Inventory class
#from AgileStockWeb.models import Inventory

 #import SQL

#an inventory object
#keyBoard = Inventory.Inventory("Keyboard", 0)
#print(f"name:{keyBoard.name:s}, itemNum:{keyBoard.itemNum}")
#an inventory object end

