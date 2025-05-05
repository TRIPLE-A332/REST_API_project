from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_path = "C:\\Users\\abdul\\OneDrive\\Documents\\GitHub\\REST_API_project\\Flask\\users.db"

#Database setup
def init_db():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name STRING NOT NULL,
            email STRING UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

#READ
def get_user():
    conn=sqlite3.connect(DB_path)
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users")
    users=cursor.fetchall()
    conn.close()
    return users

#CREATE
def add_user(name,email):
    conn=sqlite3.connect(DB_path)
    cursor=conn.cursor()
    cursor.execute('INSERT INTO users (name,email) VALUES (?,?)', (name , email))
    conn.commit()
    conn.close()

#UPDATE
def update_user(id,name,email):
    conn=sqlite3.connect(DB_path)
    cursor=conn.cursor()
    cursor.execute('UPDATE users SET name = ?, email=? WHERE id=?',(name,email,id))
    conn.commit()
    conn.close()

#DELETE
def del_user(id):
    conn=sqlite3.connect(DB_path)
    cursor=conn.cursor()
    cursor.execute('DELETE FROM users WHERE id=?', (id,))
    conn.commit()
    conn.close()

#HOME PAGE
@app.route('/')
def index():
    users = get_user()
    return render_template('index.html',users = users)

#ADD USER 
@app.route('/add_user',methods=['POST'])
def add_user_route():
    name = request.form['name']
    email= request.form['email']
    add_user(name, email)
    return redirect(url_for('index'))

#UPDATE USER
@app.route('/update_user/<int:id>', methods=['GET','POST'])
def update_user_route(id):
    if request.method=='POST':
        name = request.form['name']
        email= request.form['email']
        update_user(id,name,email)
        return redirect(url_for('index'))
    
    #calling pre filled form
    conn = sqlite3.connect(DB_path)
    cursor= conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id =?',(id,))
    user = cursor.fetchone()
    conn.close()
    return render_template('update_user.html', user=user)

#DELETE USER
@app.route('/delete_user/<int:id>', methods=['GET'])
def del_user_route(id):
    del_user(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)