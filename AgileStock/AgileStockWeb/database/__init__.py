import os
import pymysql
from AgileStockWeb.models.out_formatter import logger

# MySQL Database
# Function: create_table creates a table in MySQL database
class Database:
    def __init__(self, app):
        logger.info(f"Initializing database connection")
        self.mysql = pymysql.connect(
            host = app.config['MYSQL_HOST'],
            user = app.config['MYSQL_USER'],
            password= app.config['MYSQL_PASSWORD'],
            db = app.config['MYSQL_DB']
        )
        logger.info(f"Connection created")

    def _runSQL(self, SQLcommand):
        cursor = self.mysql.cursor()
        print(SQLcommand)
        cursor.execute(f'{SQLcommand!s}')
        self.mysql.commit()
        cursor.close()

    def runSQLfetchall(self, SQLcommand):
        cursor = self.mysql.cursor()
        print(SQLcommand)
        cursor.execute(f'{SQLcommand!s}')
        result = cursor.fetchall()
        cursor.close()
        # for row in result:
        #     print(row)
        return result

class CreateDatabase(Database):
    def __init__(self, app):
        super().__init__(app)
        self.__create_tableBOOK()
        self.__create_tableAS_ITEM()

    def __create_tableBOOK(self):
        try:
            logger.info(f"Creating 'BOOK' Table =====")
            SQLcommand = '''
                CREATE TABLE IF NOT EXISTS BOOK (
                ID INT AUTO_INCREMENT PRIMARY KEY ,
                TITLE VARCHAR(255) NOT NULL,
                AUTHOR VARCHAR(255) NOT NULL,
                PUBLISHER VARCHAR(255),
                PUBLISHED_DATE VARCHAR(255),
                GENRE VARCHAR(56) NOT NULL,
                ISBN VARCHAR(13)
                )
                '''
            self._runSQL(SQLcommand)
            logger.info(f"BOOK Table Created =====")
        except Exception as e:
            logger.error(f"Error while creating table: {e}")

    def __create_tableAS_ITEM(self):
        try:
            logger.info(f"Creating 'AS_ITEM' Table =====")
            SQLcommand = '''
                CREATE TABLE IF NOT EXISTS AS_ITEM (
                INVENTORYID INT AUTO_INCREMENT PRIMARY KEY,
                BARCODE INT,
                PRODUCTNAME VARCHAR(255) NOT NULL,
                PRODUCTCATEGORY VARCHAR(255) NOT NULL,
                INVENTORYSKU VARCHAR(255) NOT NULL
                )
                '''
            self._runSQL(SQLcommand)
            logger.info(f"AS_ITEM Table Created =====")
        except Exception as e:
            logger.error(f"Error while creating table: {e}")
            
    def insert_intoBOOK(self, title, author, publisher, publishedDate, genre, isbn):
        try:
            logger.info(f"Inserting 'BOOK' =====")
            self._runSQL(f'''
                INSERT INTO BOOK (TITLE, AUTHOR, PUBLISHER, PUBLISHED_DATE, GENRE, ISBN)
                VALUES ('{title}', '{author}', '{publisher}', '{publishedDate}', '{genre}', '{isbn}');
                ''')
            logger.info(f"BOOK Inserted ===== Title: {title}")
        except Exception as e:
            logger.error(f"Error with INSERT into table BOOK{e}")
    
    def fetch_fromAS_ITEM(self):
        try:
            logger.info(f"Inserting 'AS_ITEM' =====")
            result = self.runSQLfetchall(f'''
                SELECT * FROM AS_ITEM
            ''')
            logger.info(f"AS_ITEM successful fetch!")
            return result
        except Exception as e:
            logger.error(f"Error with INSERT into table AS_ITEM{e}")




    #TODO: Create select statement to get a book from the database
    # def select_fromBOOK(self):
    #     try:
    #         logger.info(f"Inserting 'BOOK' =====")
    #         self._runSQL(f'''
    #             SELECT * FROM BOOK
    #         ''')
    #         logger.info(f"BOOK Inserted ===== Title: {title}")
    #     except Exception as e:
    #         logger.error(f"Error with INSERT into table BOOK{e}")

    #API_InventoryFromScannerApp = AS_Item(12345, "bookofsomesort", "action", 1, "5432112345ABCD")
    def insert_intoAS_ITEM(self, barcode, productName, productCategory, inventoryID, intenvorySKU):
        try:
            logger.info(f"Inserting 'AS_ITEM' =====")
            self._runSQL(f'''
                INSERT INTO AS_ITEM (BARCODE, PRODUCTNAME, PRODUCTCATEGORY, INVENTORYID, INVENTORYSKU)
                VALUES ('{barcode}', '{productName}', '{productCategory}', '{inventoryID}', '{intenvorySKU}');
                ''')
            logger.info(f"AS_ITEM Inserted ===== ITEM: {productName}")
        except Exception as e:
            logger.error(f"Error with INSERT into table AS_ITEM{e}")
