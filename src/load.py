import pandas as pd
import sqlite3


def load():

    # Read processed data
    df = pd.read_csv("data/processed/products_clean.csv")

    # Connect to SQLite database
    conn = sqlite3.connect("data/ecommerce.db")

    # Load data into SQLite
    df.to_sql(
        "products",
        conn,
        if_exists="replace",
        index=False
    )

    # Verify loaded rows
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]

    conn.close()

    print(f"Load completed. Rows loaded: {count}")


if __name__ == "__main__":
    load()