import os
import pymysql
from AgileStockWeb.models.out_formatter import logger

# MySQL Database
# Function: create_table creates a table in MySQL database
class Database:
    def __init__(self, app):

        self.mysql = pymysql.connect(
            host = app.config['MYSQL_HOST'],
            user = app.config['MYSQL_USER'],
            password= app.config['MYSQL_PASSWORD'],
            db = app.config['MYSQL_DB']
        )
        self.__create_table()

    def __create_table(self):
        try:
            logger.info(f"Creating Table Started =====")
            cursor = self.mysql.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS items (
                    id INT AUTO_INCREMENT PRIMARY KEY ,
                    name VARCHAR(255) NOT NULL,
                    description TEXT
                )
                '''
            )
            self.mysql.commit()
            cursor.close()
            logger.info(f"Items Table Created =====")
        except Exception as e:
            logger.error(f"Error while creating table{e}")