# ==========================================
# Book Scraper Project
# Website -> Python -> Pandas -> SQLite -> Excel
# ==========================================

import os
import sqlite3
import requests
import pandas as pd
from bs4 import BeautifulSoup

# ------------------------------------------
# Create Required Folders
# ------------------------------------------

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# ------------------------------------------
# Step 1 : Scrape Website
# ------------------------------------------

def scrape():

    url = "https://books.toscrape.com/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Use response.content to avoid encoding issues
        soup = BeautifulSoup(response.content, "html.parser")

        products = soup.find_all("article", class_="product_pod")

        product_list = []

        for product in products:

            name = product.h3.a["title"]

            price = product.find(
                "p",
                class_="price_color"
            ).text

            rating = product.find(
                "p",
                class_="star-rating"
            )["class"][1]

            availability = product.find(
                "p",
                class_="instock availability"
            ).text.strip()

            product_list.append({
                "Book Name": name,
                "Price": price,
                "Rating": rating,
                "Availability": availability
            })

        return pd.DataFrame(product_list)

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
        return pd.DataFrame()

# ------------------------------------------
# Step 2 : Clean Data
# ------------------------------------------

def clean(df):

    if df.empty:
        return df

    df["Price"] = (
        df["Price"]
        .str.replace("£", "", regex=False)
        .str.replace("Â", "", regex=False)
        .astype(float)
    )

    df["Book Name"] = df["Book Name"].str.strip()
    df["Availability"] = df["Availability"].str.strip()

    return df

# ------------------------------------------
# Step 3 : Save CSV
# ------------------------------------------

def save_csv(df):

    if df.empty:
        print("No data to save.")
        return

    path = "data/products.csv"

    df.to_csv(
        path,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"CSV Saved Successfully -> {path}")

# ------------------------------------------
# Step 4 : Save SQLite Database
# ------------------------------------------

def save_database(df):

    if df.empty:
        return

    conn = sqlite3.connect("data/products.db")

    df.to_sql(
        "products",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database Saved Successfully")

# ------------------------------------------
# Step 5 : SQL Report
# ------------------------------------------

def report():

    conn = sqlite3.connect("data/products.db")

    print("\n==============================")
    print("BOOK STORE REPORT")
    print("==============================")

    print("\nTop 5 Costliest Books\n")

    query1 = """
    SELECT *
    FROM products
    ORDER BY Price DESC
    LIMIT 5
    """

    print(pd.read_sql(query1, conn))

    print("\nAverage Price\n")

    query2 = """
    SELECT ROUND(AVG(Price),2) AS Average_Price
    FROM products
    """

    print(pd.read_sql(query2, conn))

    print("\nRating Count\n")

    query3 = """
    SELECT Rating,
           COUNT(*) AS Total
    FROM products
    GROUP BY Rating
    ORDER BY Total DESC
    """

    print(pd.read_sql(query3, conn))

    conn.close()

# ------------------------------------------
# Step 6 : Save Excel
# ------------------------------------------

def save_excel(df):

    if df.empty:
        return

    path = "reports/Daily_Report.xlsx"

    df.to_excel(
        path,
        index=False
    )

    print(f"Excel Report Generated -> {path}")

# ------------------------------------------
# Main Function
# ------------------------------------------

def main():

    print("=" * 40)
    print("BOOK SCRAPER PROJECT")
    print("=" * 40)

    print("\nScraping Website...")

    df = scrape()

    if df.empty:
        print("No data found.")
        return

    print("\nFirst 5 Records\n")
    print(df.head())

    print("\nCleaning Data...")
    df = clean(df)

    print("\nSaving CSV...")
    save_csv(df)

    print("\nSaving Database...")
    save_database(df)

    print("\nSaving Excel...")
    save_excel(df)

    print("\nGenerating SQL Report...")
    report()

    print("\nProject Completed Successfully!")

# ------------------------------------------
# Run Program
# ------------------------------------------

if __name__ == "__main__":
    main()