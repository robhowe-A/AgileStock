"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify

# from AgileStockWeb import app, db
from AgileStockWeb import app, db


from AgileStockWeb.models.book import AS_BOOK

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    """Renders the home page."""
    # TODO: create code to get the book from database
    # TODO: create code to update book in the database
    AS_BOOKresult = db.fetch_fromAS_BOOK()
    if request.method == "POST":
        title = request.form["title"]
        return render_template(
            "index.html",
            title="Form",
            result=AS_BOOKresult,
            year=datetime.now().year,
        )
    if request.method == "GET":
        return render_template(
            "index.html",
            title="Inventory",
            result=AS_BOOKresult,
            year=datetime.now().year,
        )


# HTTP PUT method mockup -- untested, just sample code
# @app.route('/changetitle', methods=['GET', 'POST'])
# def changetitle():
#     """Renders a form page."""
#     # TODO: create code to get the book from database
#     # TODO: create code to update book in the database
#     if request.method == 'POST':
#         title = request.form['title']
#         return render_template('changetitle.html', title='Form', booktitle=title)
#     return render_template('changetitle.html', title='Form')


@app.route("/contact")
def contact():
    """Renders the contact page."""
    return render_template(
        "contact.html",
        title="Contact",
        year=datetime.now().year,
        message="Get in touch with our skilled team.",
    )


@app.route("/about")
def about():
    """Renders the about page."""
    return render_template(
        "about.html",
        title="About",
        year=datetime.now().year,
        message="Agile Stock inventory.",
    )


@app.route("/editbook")
def editBook():
    """Renders the edit page."""
    if request.method == "GET":
        # print(f'the url data: {request.args["isbn"]}')
        # request.args gets the passed in isbn value. this value is the isbn of the book who's edit button was clicked.
        return render_template(
            "editBook.html",
            title="Edit",
            year=datetime.now().year,
            message="Agile Stock inventory.",
        )


#################################  API  #################################


@app.route("/api/inventoryitem", methods=["GET", "POST"])
def entities():
    if request.method == "GET":
        return {"AS_BOOK(s)": db.fetch_fromAS_BOOK()}  # returns db data from fetch
    if request.method == "POST":
        print(f"request is: {request.json}")
        item = AS_BOOK(
            request.json["TITLE"],
            request.json["AUTHOR"],
            request.json["PUBLISHER"],
            request.json["PUBLISHED_DATE"],
            request.json["GENRE"],
            request.json["ISBN"],
        )
        print(f"book title to add: {item.title}")
        print(f"book genre to add: {item.genre}")
        print(f"book isbn to add: {item.isbn}")
        print(f"book title to add: {item.publishedDate}")
        db.insert_intoAS_BOOK(
            item.isbn,
            item.title,
            item.author,
            item.publisher,
            item.publishedDate,
            item.genre,
        )  # inserts a new item into db
        return {"AS_BOOK": request.json}


@app.route("/api/inventoryitem/<int:entity_id>", methods=["GET", "PUT", "DELETE"])
def entity(entity_id):
    print("test")
    if request.method == "GET":
        return db.select_fromINVENTORY_ID(entity_id)

    # if request.method == "PUT":
    #     return {
    #         'id': entity_id,
    #         'message': 'This endpoint should update the entity {}'.format(entity_id),
    #         'method': request.method,


# 	'body': request.json
#     }
# if request.method == "DELETE":
#     return {
#         'id': entity_id,
#         'message': 'This endpoint should delete the entity {}'.format(entity_id),
#         'method': request.method
#     }


@app.route("/api/inventoryitem/isbnsearch/<int:book_isbn>", methods=["GET"])
def book(book_isbn):
    if request.method == "GET":
        print("Entering function")
        book = db.select_fromINVENTORY_ISBN(book_isbn)
        return book


# @app.route('/api/delete/inventoryitem', methods=['GET', 'POST'])
# @app.route('/api/delete/inventoryitem/<int:entity_id>', methods=['GET', 'POST'])
