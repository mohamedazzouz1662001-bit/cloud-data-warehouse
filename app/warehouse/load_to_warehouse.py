import os

import pandas as pd
import psycopg2
from dotenv import load_dotenv

from app.db.connect import get_connection


load_dotenv()


def load_to_warehouse():
    source_conn = get_connection()
    source_df = pd.read_sql("SELECT * FROM sales ORDER BY order_date;", source_conn)
    source_conn.close()

    warehouse_host = os.getenv("WAREHOUSE_HOST")
    warehouse_db = os.getenv("WAREHOUSE_NAME")
    warehouse_user = os.getenv("WAREHOUSE_USER")
    warehouse_password = os.getenv("WAREHOUSE_PASSWORD")
    warehouse_port = os.getenv("WAREHOUSE_PORT", "5432")

    if not all([warehouse_host, warehouse_db, warehouse_user, warehouse_password]):
        raise ValueError("Please configure warehouse environment variables in .env")

    warehouse_conn = psycopg2.connect(
        host=warehouse_host,
        port=warehouse_port,
        dbname=warehouse_db,
        user=warehouse_user,
        password=warehouse_password,
    )

    # Create a target table in the warehouse if it does not exist
    create_sql = """
    CREATE TABLE IF NOT EXISTS sales_warehouse (
        id INTEGER,
        order_id VARCHAR(100),
        customer_name VARCHAR(100),
        product_name VARCHAR(100),
        quantity INT,
        total_amount NUMERIC(10,2),
        order_date DATE
    );
    """
    with warehouse_conn.cursor() as cur:
        cur.execute(create_sql)
        for _, row in source_df.iterrows():
            cur.execute(
                """
                INSERT INTO sales_warehouse (id, order_id, customer_name, product_name, quantity, total_amount, order_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    row["id"],
                    row["order_id"],
                    row["customer_name"],
                    row["product_name"],
                    row["quantity"],
                    row["total_amount"],
                    row["order_date"],
                ),
            )
        warehouse_conn.commit()

    warehouse_conn.close()
    print(f"Loaded {len(source_df)} rows to warehouse successfully.")


if __name__ == "__main__":
    load_to_warehouse()
