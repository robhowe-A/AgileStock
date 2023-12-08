"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
# from AgileStockWeb import app, db
from AgileStockWeb import app, db


from AgileStockWeb.models.book import Book, AS_Item
from AgileStockWeb import wolfBook, AS_ITEMresult

NewTitle = []

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    # TODO: create code to get the book from database
    # TODO: create code to update book in the database
    print(type(AS_ITEMresult))
    if request.method == 'POST':
        title = request.form['title']
        NewTitle.append(title)
        wolfBook.title = title
        return render_template('index.html',
                               title='Form',
                               testBookN = wolfBook,
                               )
    else:
        return render_template(
            'index.html',
            title='Inventory',
            testBookN = wolfBook,
            result = AS_ITEMresult[0],
            year=datetime.now().year,
        )

@app.route('/changetitle', methods=['GET', 'POST'])
def changetitle():
    """Renders a form page."""
    # TODO: create code to get the book from database
    # TODO: create code to update book in the database
    if request.method == 'POST':
        title = request.form['title']
        NewTitle.append(title)
        return render_template('changetitle.html', title='Form', booktitle=title)
    return render_template('changetitle.html', title='Form')


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
#################################  API  #################################
import json 

@app.route('/basic_api/inventoryitem', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'message': 'This endpoint returns a list of inventory items',
            'method': request.method
        }
    if request.method == "POST":
        print(f"Inbound string: {request.json}")
        #itemstr = json.loads(request.json)
        item = AS_Item(
            request.json["barcode"],
            request.json["productName"],
            request.json["productCategory"],
            request.json["inventorySKU"])
        print(item.inventorySKU)
        db.insert_intoAS_ITEM(item.barcode, item.productName, item.productCategory, item.inventorySKU)
        return {
            'message': 'This endpoint creates an inventory item',
            'method': request.method,
		'body': request.json
        }

@app.route('/basic_api/inventoryitem/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message': 'This endpoint should return the entity {} details'.format(entity_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': entity_id,
            'message': 'This endpoint should update the entity {}'.format(entity_id),
            'method': request.method,
		'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': entity_id,
            'message': 'This endpoint should delete the entity {}'.format(entity_id),
            'method': request.method
        }