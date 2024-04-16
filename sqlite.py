import sqlite3
import json

# Load the JSON data
with open('extracted_data.json') as json_file:
    data = json.load(json_file)

# Connect to the SQLite database (if it doesn't exist, it will be created)
conn = sqlite3.connect('products.db')

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Create a table to store product data
cur.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price TEXT,
                brand TEXT,
                image_url TEXT,
                product_url TEXT
            )''')

# Insert data into the table
for product_id, product_data in data.items():
    cur.execute('''INSERT INTO products (name, price, brand, image_url, product_url)
                    VALUES (?, ?, ?, ?, ?)''',
                (product_data['Name'], product_data['Price'], product_data['Brand'], product_data['Image URL'], product_data['Product URL']))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Database and table created successfully.")