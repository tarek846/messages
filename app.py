from flask import Flask, render_template, request
import sqlite3

x = sqlite3.connect('database.db')
cursor = x.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
               )
''')
x.commit()
x.close()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        n = request.form['name']
        e = request.form['email']
        m = request.form['message']
        return render_template('thank_you.html', name=n)
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=1)






