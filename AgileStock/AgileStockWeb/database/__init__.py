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

class CreateDatabase(Database):
    def __init__(self, app):
        super().__init__(app)
        self.__create_table()

    def __create_table(self):
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
            
    def insert_intoBOOK(self, title, author, publisher, publishedDate, genre, isbn):
        try:
            logger.info(f"Inserting 'BOOK' =====")
            self._runSQL(f'''
                INSERT INTO BOOK (TITLE, AUTHOR, PUBLISHER, PUBLISHED_DATE, GENRE, ISBN)
                VALUES ('{title}', '{author}', '{publisher}', '{publishedDate}', '{genre}', '{isbn}');
                ''')
            logger.info(f"BOOK Inserted ===== Title: {title}")
        except Exception as e:
            logger.error(f"Error while creating table{e}")
