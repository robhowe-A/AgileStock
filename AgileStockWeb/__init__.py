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


from flask import Flask, request, jsonify

app = Flask(__name__)

import AgileStockWeb.views

import os
import pymysql
# #SQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '4LocalDB'
app.config['MYSQL_DB'] = 'agilestockinv'

mysql = pymysql.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password= app.config['MYSQL_PASSWORD'],
    db = app.config['MYSQL_DB']
)


def create_table():
    try:
        print('Creating Table Started =====')
        cur = mysql.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY ,
                name VARCHAR(255) NOT NULL,
                description TEXT
            )
            '''
        )
        mysql.commit()
        cur.close()
        print('Items Table Created =====')
    except Exception as e:
        print("Error while creating table",e)

create_table()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username


# #an inventory object
# #keyBoard = Inventory.Inventory("Keyboard", 0)
# #print(f"name:{keyBoard.name:s}, itemNum:{keyBoard.itemNum}")
# #an inventory object end

