import pymysql
from AgileStockWeb.models.out_formatter import logger


# MySQL Database
# Function: create_table creates a table in MySQL database
class Database:
    def __init__(self, app):
        logger.info(f"Initializing database connection")
        self.mysql = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB'],
            ssl_disabled=True  #DEVELOPMENT ONLY
        )   
        logger.info(f"Connection created")

    def _runSQL(self, SQLcommand):
        cursor = self.mysql.cursor()
        print(SQLcommand)
        cursor.execute(f'{SQLcommand!s}')
        self.mysql.commit()
        cursor.close()

    def _runSQLfetchall(self, SQLcommand):
        cursor = self.mysql.cursor()
        print(SQLcommand)
        cursor.execute(f'{SQLcommand!s}')
        result = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in result]
        cursor.close()
        # for row in result:
        #     print(row)
        return data

class CreateDatabase(Database):
    def __init__(self, app):
        super().__init__(app)
        self.__create_tableAS_BOOK()

    def __create_tableAS_BOOK(self):
        try:
            logger.info(f"Creating 'AS_BOOK' Table =====")
            SQLcommand: str = '''
                CREATE TABLE IF NOT EXISTS AS_BOOK (
                BOOKID INT AUTO_INCREMENT PRIMARY KEY,
                ISBN VARCHAR(255) NOT NULL UNIQUE,
                TITLE VARCHAR(255) NOT NULL,
                AUTHOR VARCHAR(255) NOT NULL,
                PUBLISHER VARCHAR(255) NOT NULL,
                PUBLISHED_DATE VARCHAR(255),
                GENRE VARCHAR(255)
                )
                '''
            self._runSQLfetchall(SQLcommand)
            logger.info(f"AS_BOOK Table Created =====")
        except Exception as e:
            logger.error(f"Error while creating table: {e}")

    def fetch_fromAS_BOOK(self):
        try:
            logger.info(f"Selecting 'AS_BOOK' =====")
            result = self._runSQLfetchall(f'''
                SELECT * FROM AS_BOOK
            ''')
            logger.info(f"AS_BOOK successful fetch!")
            return result
        except Exception as e:
            logger.error(f"Error with SELECT for table AS_BOOK: {e}")

    def select_fromINVENTORY_ID(self, ID):
        try:
            logger.info(f"Retrieving 'BOOK' =====")
            s = self._runSQLfetchall(f'''
                SELECT * FROM AS_BOOK WHERE BOOKID = {ID}
            ''')
            print(s[0]["ISBN"])
            logger.info(f"AS_BOOK Retrieved ===== Title: {s[0]['ISBN']}")
            return s
            
        except Exception as e:
            logger.error(f"Error with RETRIEVE into table BOOK {e} ")

    def insert_intoAS_BOOK(self, isbn, title, author, publisher, publishDate, genre):
        try:
            logger.info(f"Inserting 'AS_BOOK' =====")
            self._runSQL(f'''
                INSERT INTO AS_BOOK (ISBN, TITLE, AUTHOR, PUBLISHER, PUBLISHED_DATE, GENRE)
                VALUES ('{isbn}', '{title}', '{author}', '{publisher}', '{publishDate}', '{genre}');
                ''')
            logger.info(f"AS_BOOK Inserted ===== ITEM: {isbn}")
        except Exception as e:
            logger.error(f"Error with INSERT into table AS_BOOK: {e}")
