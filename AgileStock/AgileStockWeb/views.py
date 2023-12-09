"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify
# from AgileStockWeb import app, db
from AgileStockWeb import app, db


from AgileStockWeb.models.book import AS_Item
from AgileStockWeb import wolfBook


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    # TODO: create code to get the book from database
    # TODO: create code to update book in the database
    AS_ITEMresult = db.fetch_fromAS_ITEM()
    print(f"type: {type(AS_ITEMresult)}, length: {len(AS_ITEMresult)}")
    if request.method == 'POST':
        title = request.form['title']
        wolfBook.title = title
        return render_template('index.html',
                               title='Form',
                               testBookN = wolfBook,
                               )
    if request.method == 'GET':
        print(f"result: {AS_ITEMresult}")
        return render_template(
            'index.html',
            title='Inventory',
            testBookN = wolfBook,
            result = AS_ITEMresult,
            year=datetime.now().year,
        )

@app.route('/changetitle', methods=['GET', 'POST'])
def changetitle():
    """Renders a form page."""
    # TODO: create code to get the book from database
    # TODO: create code to update book in the database
    if request.method == 'POST':
        title = request.form['title']
        return render_template('changetitle.html', title='Form', booktitle=title)
    return render_template('changetitle.html', title='Form')


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Get in touch with our skilled team.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Agile Stock inventory.'
    )
#################################  API  #################################

@app.route('/api/inventoryitem', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'AS_Item(s)': db.fetch_fromAS_ITEM() #returns db data from fetch
        }
    if request.method == "POST":
        item = AS_Item(
            request.json["barcode"],
            request.json["productName"],
            request.json["productCategory"],
            request.json["inventorySKU"])
        db.insert_intoAS_ITEM(item.barcode, item.productName, item.productCategory, item.inventorySKU) #inserts a new item into db
        return {
		'AS_Item': request.json
        }

@app.route('/api/inventoryitem/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
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