import os

import pandas as pd
import psycopg2
from dotenv import load_dotenv

from app.db.connect import get_connection


load_dotenv()


def extract_sales():
    conn = get_connection()
    query = "SELECT * FROM sales ORDER BY order_date;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


if __name__ == "__main__":
    df = extract_sales()
    print(df.head())
    print(f"\nTotal rows extracted: {len(df)}")
