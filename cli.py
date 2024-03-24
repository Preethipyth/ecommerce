import argparse
from .post_processing import derive_features
from .mysql_utils import run_sql_query


def main():
    parser = argparse.ArgumentParser(description="Run SQL queries by name")
    parser.add_argument("query_name", help="Name of the SQL query to run")
    parser.add_argument("window_type", help="Window type (e.g., daily)")
    parser.add_argument("start_date", help="Start date of the window (YYYY-MM-DD)")
    parser.add_argument("end_date", help="End date of the window (YYYY-MM-DD)")
    parser.add_argument("category", help="Category for filtering the data")
    args = parser.parse_args()

    print("Query Name:", args.query_name)
    print("Window Type:", args.window_type)
    print("Start Date:", args.start_date)
    print("End Date:", args.end_date)
    print("Category:", args.category)

    rows = run_sql_query(args.query_name, args.window_type, args.start_date, args.end_date, args.category)

    print("Derived Features:")
    total_orders,popular_item,max_orders = derive_features(rows)
    
    print(f"Total Orders: {total_orders}")
    print(f"Popular Item: {popular_item} (Ordered {max_orders} times)")

