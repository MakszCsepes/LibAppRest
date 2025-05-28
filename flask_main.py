# flask
# flask_session
# psycopg2


from flask import Flask, render_template, redirect, request, session
from flask_session import Session
import psycopg2 

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)



# db connection
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='',
    user='postgres',
    password='makszpass'
)
    





# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('index.html', title='HOME')
 

@app.route('/books')
# ‘/’ URL is bound with hello_world() function.
def books():
    print('user: ' + session['username'])
    # db connection
    cur = conn.cursor()
    
    cur.execute("SELECT title, author.surname as author, year from books join author on books.author_id = author.author_id;")    
    
    books_lst = []
    for row in cur.fetchall():
        books_lst.append(
            {
                'title': row[0],
                'author': row[1],
                'year': row[2],
            }
        )

    # FORMAT
    #books_lst = [{'title': 'Martin Eden', 'author': 'Jack London', 'year': 1905},
     #            {'title': 'Two Towers', 'author': 'John Tolkien', 'year': 1955},
      #           {'title': 'The Last of the Mohicans', 'author': 'Fenimore Cooper', 'year': 1887}]
    books_json = {'books': books_lst}
    
    return render_template('books.html', obj=books_json)

@app.route('/books/<name>')
def book(name):
    cur = conn.cursor()
    cur.execute("SELECT title, author.surname as author, year, genre.name as genre from books join author on books.author_id = author.author_id join genre on books.genre_id = genre.genre_id where title = '" + str(name) + "';")    
    
    val = cur.fetchone()
    books_lst = [
        {
            'title': val[0],
            'author': val[1],
            'year': val[2],
            'genre': val[3],
        }
                  ]

    books_json = {'books': books_lst}
    
    return render_template('books.html', obj=books_json)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        
        session['username'] = request.form['name']
        
        return redirect('/books')

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()