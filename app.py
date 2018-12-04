from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    value = 12
    return second_method(value)

def second_method(arg):
    return render_template('home.html', value = arg)

@app.route('/invoice', methods=['POST'])
def invoice():
    conn = sqlite3.connect('invoices.db')
    cur = conn.cursor()
    if request.method == "POST":
        inv = request.form['inv']
        amount = request.form['amount']
        if inv == "":
            return "<h1> OPPS! Field can not be blank</h1>"
        cur.execute("INSERT INTO invoices VALUES (null, ?,?)", (inv.lower(), amount))
        conn.commit()
        return home()
    return home()

@app.route('/return_invoices', methods=['GET'])
def return_invoices():
    conn = sqlite3.connect('invoices.db')
    cur = conn.cursor()
    all_invoices = cur.execute('SELECT * FROM invoices;').fetchall()
    return jsonify(all_invoices)

if __name__=='__main__':
    app.debug = True
    app.run()