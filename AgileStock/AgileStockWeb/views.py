"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
# from AgileStockWeb import app, db
from AgileStockWeb import app, db


from AgileStockWeb.models.book import Book
from AgileStockWeb import wolfBook

NewTitle = []

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    # TODO: create code to get the book from database
    # TODO: create code to update book in the database
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
