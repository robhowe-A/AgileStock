"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect

# from AgileStockWeb import app, db
from AgileStockWeb import app, db


from AgileStockWeb.models.book import AS_BOOK

# def update_book_database_all(entity_id):
#     db.edit_title_AS_BOOK(request.json[0]["TITLE"], entity_id)
#     db.edit_author_AS_BOOK(request.json[0]["AUTHOR"], entity_id)
#     db.edit_published_date_AS_BOOK(request.json[0]["PUBLISHED_DATE"], entity_id)
#     db.edit_publisher_AS_BOOK(request.json[0]["PUBLISHER"], entity_id)
#     db.edit_genre_AS_BOOK(request.json[0]["GENRE"], entity_id)


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


@app.route("/editbook", methods=["GET", "POST"])
def editBook():
    """Renders the edit page."""
    if request.method == "GET":
        # print(f'the url data: {request.args["isbn"]}')
        # request.args gets the passed in isbn value. this value is the isbn of the book who's edit button was clicked.
        # when the user loads the edit page, the isbn is passed through URL query parameter
        # the isbn is searched in our database to return the object attributes
        cur_isbn = request.args["isbn"]
        returnBookObj = db.select_fromINVENTORY_ISBN(cur_isbn)

        item = AS_BOOK(
            returnBookObj[0]["TITLE"],
            returnBookObj[0]["AUTHOR"],
            returnBookObj[0]["PUBLISHER"],
            returnBookObj[0]["PUBLISHED_DATE"],
            returnBookObj[0]["GENRE"],
            returnBookObj[0]["ISBN"],
        )

        return render_template(
            "editBook.html",
            title="Edit",
            year=datetime.now().year,
            message="Agile Stock inventory.",
            book_to_edit=item,
        )

    # Editbook page has a form to submit. We need logic to pass the book id or isbn, then
    # complete the change.
    if request.method == "POST":
        try:
            entity_id = db.select_fromINVENTORY_ISBN(request.args['isbn'])

            #Since editform has a post, each attribute is edited from data ingress
            db.edit_title_AS_BOOK(request.form["title"], entity_id[0]['BOOKID'])
            db.edit_author_AS_BOOK(request.form["author"], entity_id[0]['BOOKID'])
            db.edit_published_date_AS_BOOK(request.form["publishedDate"], entity_id[0]['BOOKID'])
            db.edit_publisher_AS_BOOK(request.form["publisher"], entity_id[0]['BOOKID'])
            db.edit_genre_AS_BOOK(request.form["genre"], entity_id[0]['BOOKID'])


            #updates have succeeded, fetch the list of inventory and redirect user to inv page
            AS_BOOKresult = db.fetch_fromAS_BOOK()

            return render_template(
            "index.html",
            title="Inventory",
            result=AS_BOOKresult,
            year=datetime.now().year,
        )
        except:
            return {"Server error": "The book's update could not process successfully."}


#################################  API  #################################


@app.route("/api/inventoryitem", methods=["GET", "POST"])
def entities():
    if request.method == "GET":
        return {"AS_BOOK(s)": db.fetch_fromAS_BOOK()}  # returns db data from fetch
    if request.method == "POST":
        item = AS_BOOK(
            request.json[0]["TITLE"],
            request.json[0]["AUTHOR"],
            request.json[0]["PUBLISHER"],
            request.json[0]["PUBLISHED_DATE"],
            request.json[0]["GENRE"],
            request.json[0]["ISBN"],
        )
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
    if request.method == "GET":
        return db.select_fromINVENTORY_ID(entity_id)

    if request.method == "PUT":
        # Logic for updating a database object

        db.edit_title_AS_BOOK(request.json[0]["TITLE"], entity_id)
        db.edit_author_AS_BOOK(request.json[0]["AUTHOR"], entity_id)
        db.edit_published_date_AS_BOOK(request.json[0]["PUBLISHED_DATE"], entity_id)
        db.edit_publisher_AS_BOOK(request.json[0]["PUBLISHER"], entity_id)
        db.edit_genre_AS_BOOK(request.json[0]["GENRE"], entity_id)

        return {
            "id": entity_id,
            "message": f"Updated database entity if this request response == 200.",
            "method": request.method,
        }
    
    if request.method == "DELETE":
        #match the URL id to the JSON id, requested for delete
        if entity_id == int(request.json[0]["delete_book_id"]):
            
            #call database function to delete the item
            db.delete_AS_BOOK(request.json[0]["delete_book_id"])
            return {
                "id": entity_id,
                "message": f"Deleted database entity if this request response == 200.",
                "method": request.method,
            }
        else:
            #unsuccessful database operation: return json message to caller
            return {
                "id": entity_id,
                "message": f"Delete method called. Unable to delete the item due to ID mismatch.",
                "entity_id": entity_id,
                "BOOKID": request.json[0]["delete_book_id"]
            }


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

@app.route("/API/Delete", methods=['POST'])
def delete_Book():
    print ("Deleting book . . .")
    print (request.form["delete_book"])
    #entity_id = db.select_fromINVENTORY_ISBN(request.args['isbn'])
    db.delete_AS_BOOK(request.form["delete_book"])
    return redirect(request.referrer)