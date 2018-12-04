from flask import Flask, request, jsonify
import sqlite3


conn = sqlite3.connect('invoices.db')
print("opened database connection successfully")

conn.execute(''' CREATE TABLE invoices
            (ID INTEGER PRIMARY KEY,
            invoice_name TEXT NOT NULL,
            invoice_amount INT NOT NULL);''')

print("Table created successfully")

conn.close()