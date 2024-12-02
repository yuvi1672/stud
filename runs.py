from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Reset@123",
    database="Student_db"
)

@app.route('/')
def index():
    return render_template('index.html')  # Save the above HTML in a templates folder as 'index.html'

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']

    cursor = db.cursor()
    sql = "INSERT INTO students (name, email, phone, course) VALUES (%s, %s, %s, %s)"
    values = (name, email, phone, course)
    
    try:
        cursor.execute(sql, values)
        db.commit()
        flash("Registration successful!", "success")
    except mysql.connector.Error as err:
        db.rollback()
        flash(f"Error: {err}", "danger")
    finally:
        cursor.close()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
