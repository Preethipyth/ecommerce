import logging
from mysql.connector import *
import datetime

# Set up logging
logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_mysql():
    try:
        db = connect(host='localhost', user='root', password='root', db='ecommerce', port='3306')
        return db
    except Error as e:
        logging.error(f"Error connecting to MySQL: {e}")

def run_sql_query(query_name, window_type, start_date, end_date, category):
    try:
        if window_type == 'daily':
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date() + datetime.timedelta(days=1)
        else:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d %H").replace(minute=0, second=0)
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d %H").replace(minute=0, second=0) + datetime.timedelta(hours=1)

        conn = connect_to_mysql()
        cursor = conn.cursor()

        sql_query = {"demand": """
            SELECT *
            FROM orders
            WHERE InvoiceDate >= %s AND InvoiceDate < %s
            AND Description LIKE %s
        """
        }
        if query_name in sql_query:
            cursor.execute(sql_query[query_name], (start_date, end_date, f'%{category}%'))
            rows = cursor.fetchall()
            logging.info(f"Query executed: {query_name}")
        return rows

    except Error as e:
        logging.error(f"Error running SQL query: {e}")
    finally:
        cursor.close()
