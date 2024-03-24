from mysql.connector import *
import datetime

def connect_to_mysql():
    db = connect(host='localhost',user = 'root',password='root',db='ecommerce_analyzer',port ='3306')
    return db

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

        sql_query = {"demand" : """
            SELECT *
            FROM orders
            WHERE InvoiceDate >= %s AND InvoiceDate < %s
            AND Description LIKE %s
        """
        }
        if query_name in sql_query:
            cursor.execute(sql_query[query_name], (start_date, end_date, f'%{category}%'))
            rows = cursor.fetchall()
            # print(rows)
        return rows

    except:
        print("Error:")

    finally:
       cursor.close()