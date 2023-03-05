from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__, template_folder="./")

# configure MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'your_database_name'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

# define a route to display the voting form
@app.route('/')
def voting_form():
    return render_template('voterForm.html')

# define a route to process the submitted form data
@app.route('/', methods=['POST'])
def submit_vote():
    candidate = request.form['candidate']

    # store the vote in the database
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO votes (candidate) VALUES (%s)", (candidate,))
    conn.commit()
    conn.close()

    return "Vote submitted successfully!"

if __name__ == '__main__':
    app.run()
