##########################################################################
## Company: AgileStock
## Engineer(s): Robert Howell, Branson Addington, David Poach
## 
## Create Date:    12/3/2023
## Project Name:    AgileStock
## Target Devices:    Web
## Tool versions:    MySQL >= 5.7
## Description:   Database class provides methods to create and change database tables/items in MySQL.
## Dependencies:
##   -module(s):
##      pymysql
##      AgileStockWeb.models.out_formatter
##      AgileStockWeb
##
##   -packages(s):
##      PyMySQL==1.1.0
##
## Revision: 1.3 - Confirm code runs with unit tests
## Revision: 1.2 - Added book editing SQL run functions
## Revision: 1.1 - Added select_fromINVENTORY_ISBN SQL fetch function
## Revision: 1.0 - File Created
## Additional Comments: CreateDatabase inherits Database and provides functions for the parent
##  database functions to run SQL statements.
##  Requirements: https://pymysql.readthedocs.io/en/latest/user/installation.html
##
##########################################################################

import pymysql, os
from AgileStockWeb.models.out_formatter import logger
from AgileStockWeb import app


# MySQL Database
# Function: create_table creates a table in MySQL database
class Database:
    def __init__(self, app):
        self.__host = app.config["MYSQL_HOST"]
        self.__user = app.config["MYSQL_USER"]
        self.__password = app.config["MYSQL_PASSWORD"]
        self.__db = app.config["MYSQL_DB"]

        logger.info(f"Initializing database connection")
        # Database connection context
        self.__mysql = pymysql.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            db=self.__db,
            ssl_disabled=True,  # DEVELOPMENT ONLY
        )
        logger.info(f"Connection created")

    def _runSQL(self, SQLcommand):
        cursor = self.__mysql.cursor()
        print(SQLcommand)
        cursor.execute(f"{SQLcommand!s}")
        self.__mysql.commit()
        cursor.close()

    def _runSQLfetchall(self, SQLcommand):
        cursor = self.__mysql.cursor()
        print(SQLcommand)
        cursor.execute(f"{SQLcommand!s}")
        result = cursor.fetchall()

        # return the result or "Not Found"
        if len(result) <= 0:
            data = "No results from database fetch."
        else:
            # format the result fetch into a manageable format
            columns = [column[0] for column in cursor.description]
            data = [dict(zip(columns, row)) for row in result]
            cursor.close()
        return data


class CreateDatabase(Database):
    def __init__(self, app):
        super().__init__(app)
        self.__create_tableAS_BOOK()

    def __create_tableAS_BOOK(self):
        try:
            logger.info(f"Creating 'AS_BOOK' Table =====")
            SQLcommand: str = """
                CREATE TABLE IF NOT EXISTS AS_BOOK (
                BOOKID INT AUTO_INCREMENT PRIMARY KEY,
                ISBN VARCHAR(255) NOT NULL UNIQUE,
                TITLE VARCHAR(255) NOT NULL,
                AUTHOR VARCHAR(255) NOT NULL,
                PUBLISHER VARCHAR(255) NOT NULL,
                PUBLISHED_DATE VARCHAR(255),
                GENRE VARCHAR(255)
                )
                """
            self._runSQLfetchall(SQLcommand)
            logger.info(f"AS_BOOK Table Created =====")
        except Exception as e:
            logger.error(f"Error while creating table: {e}")

    def fetch_fromAS_BOOK(self):
        try:
            logger.info(f"Selecting 'AS_BOOK' =====")
            result = self._runSQLfetchall(
                f"""
                SELECT * FROM AS_BOOK
            """
            )
            logger.info(f"AS_BOOK successful fetch!")
            return result
        except Exception as e:
            logger.error(f"Error with SELECT for table AS_BOOK: {e}")

    def select_fromINVENTORY_ID(self, ID):
        try:
            logger.info(f"Retrieving 'BOOK' =====")
            s = self._runSQLfetchall(
                f"""
                SELECT * FROM AS_BOOK WHERE BOOKID = {ID}
            """
            )
            logger.info(f"AS_BOOK Retrieved ===== ISBN: {s[0]['ISBN']}")
            return s

        except Exception as e:
            logger.error(f"Error with RETRIEVE into table AS_BOOK {e} ")

    def select_fromINVENTORY_ISBN(self, ISBN):
        try:
            logger.info(f"Retrieving 'BOOK' with ISBN {ISBN} ====")
            s = self._runSQLfetchall(
                f"""
                SELECT * FROM AS_BOOK WHERE ISBN like '{ISBN}'
            """
            )
            if isinstance(s, list):
                logger.info(f"AS_BOOK Retrieved ===== ISBN: {s[0]['ISBN']}")
                return s
            else:
                appendError = (
                    f"A book with the isbn '{ISBN}' does not exist in the database."
                )
                return [
                    {
                        "fetchSuccess": "False",
                        "errorMessage": f"{'{} {}'.format(s, appendError)}",
                    }
                ]
        except Exception as e:
            logger.error(f"Error with RETRIEVE into table BOOK {e} ")

    def insert_intoAS_BOOK(self, isbn, title, author, publisher, publishDate, genre):
        try:
            logger.info(f"Inserting 'AS_BOOK' =====")
            self._runSQL(
                f"""
                INSERT INTO AS_BOOK (ISBN, TITLE, AUTHOR, PUBLISHER, PUBLISHED_DATE, GENRE)
                VALUES ('{isbn}', '{title}', '{author}', '{publisher}', '{publishDate}', '{genre}');
                """
            )
            logger.info(f"AS_BOOK Inserted ===== ITEM: {isbn}")
        except Exception as e:
            logger.error(f"Error with INSERT into table AS_BOOK: {e}")

    def edit_title_AS_BOOK(self, title, entity_id):
        try:
            logger.info(f"Changing title to {title}")
            self._runSQL(
                f"""UPDATE AS_BOOK SET TITLE = "{title}" WHERE BOOKID = {entity_id}"""
            )
        except Exception as e:
            logger.error(f"Error with SET into table AS_BOOK: {e}")

    def edit_author_AS_BOOK(self, author, entity_id):
        try:
            logger.info(f"Changing author to {author}")
            self._runSQL(
                f"""UPDATE AS_BOOK SET AUTHOR = "{author}" WHERE BOOKID = {entity_id}"""
            )
        except Exception as e:
            logger.error(f"Error with SET into table AS_BOOK: {e}")

    def edit_publisher_AS_BOOK(self, publisher, entity_id):
        try:
            logger.info(f"Changing publisher to {publisher}")
            self._runSQL(
                f"""UPDATE AS_BOOK SET PUBLISHER = "{publisher}" WHERE BOOKID = {entity_id}"""
            )
        except Exception as e:
            logger.error(f"Error with SET into table AS_BOOK: {e}")

    def edit_published_date_AS_BOOK(self, publishedDate, entity_id):
        try:
            logger.info(f"Changing published date to {publishedDate}")
            self._runSQL(
                f"""UPDATE AS_BOOK SET PUBLISHED_DATE = "{publishedDate}" WHERE BOOKID = {entity_id}"""
            )
        except Exception as e:
            logger.error(f"Error with SET into table AS_BOOK: {e}")

    def edit_genre_AS_BOOK(self, genre, entity_id):
        try:
            logger.info(f"Changing genre to {genre}")
            self._runSQL(
                f"""UPDATE AS_BOOK SET GENRE = "{genre}" WHERE BOOKID = {entity_id}"""
            )
        except Exception as e:
            logger.error(f"Error with SET into table AS_BOOK: {e}")

    def delete_AS_BOOK(self, entity_id):
        try:
            logger.info(f"Deleting book...")
            self._runSQL(
                f"""DELETE FROM AS_BOOK WHERE BOOKID = {entity_id}"""
            )
        except Exception as e:
            logger.error(f"Error with DELETE from table AS_BOOK: {e}")
