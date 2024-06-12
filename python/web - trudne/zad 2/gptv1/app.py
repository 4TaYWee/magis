from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Funkcja tworząca tabelę komentarzy w bazie danych
def create_table():
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS comments 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, comment TEXT)''')
    conn.commit()
    conn.close()

# Dodanie komentarza do bazy danych
def add_comment(name, comment):
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute("INSERT INTO comments (name, comment) VALUES (?, ?)", (name, comment))
    conn.commit()
    conn.close()

# Pobranie wszystkich komentarzy z bazy danych
def get_comments():
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute("SELECT * FROM comments")
    comments = c.fetchall()
    conn.close()
    return comments

# Strona główna z formularzem do dodawania komentarzy
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        add_comment(name, comment)
        return redirect(url_for('index'))
    comments = get_comments()
    return render_template('index.html', comments=comments)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
