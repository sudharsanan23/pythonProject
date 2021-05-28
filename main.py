from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'task'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        details = request.form
        rollno = details['rollno']
        age = details['age']
        dept = details['dept']
        mobileno = details['mobileno']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sudharsan(rollno,age,dept,mobileno) VALUES (%s,%s,%s, %s)",
                    (rollno, age, dept, mobileno))
        mysql.connection.commit()
        cur.close()
    return jsonify({
        "rollno": rollno,
        "age": age,
        "dept": dept,
        "mobileno": mobileno
    })


@app.route('/INDEX', methods=['GET'])
def Index():
    if request.method == "GET":
        details = request.form
        rollno = details['rollno']
        cur = mysql.connection.cursor()
        cur.execute("SELECT  rollno,age,dept,mobileno FROM sudharsan where rollno=%s", (rollno,))
        output = cur.fetchall()
        cur.close()
    return jsonify(output)


@app.route('/particular', methods=['GET'])
def select():
    cur = mysql.connection.cursor()
    SQL = "SELECT * from sudharsan"
    cur.execute(SQL)
    output = cur.fetchall()
    cur.close()
    return jsonify(output)


@app.route('/delete', methods=['GET', 'POST', 'DELETE'])
def delete():
    details = request.form
    rollno = details['rollno']
    cur = mysql.connection.cursor()
    cur.execute("delete from sudharsan where rollno=%s ", (rollno,))
    cur.execute("select * from sudharsan")
    output = cur.fetchall()
    cur.close()
    return jsonify(output)


@app.route('/update', methods=['GET', 'POST', 'DELETE'])
def update():
    details = request.form
    rollno = details['rollno']
    age = details['age']
    dept = details['dept']
    mobileno = details['mobileno']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE sudharsan SET age=%s, dept=%s, mobileno=%s WHERE rollno=%s ", (age, dept, mobileno, rollno))
    mysql.connection.commit()
    return jsonify({
        "rollno": rollno,
        "age": age,
        "dept": dept,
        "mobileno": mobileno
    })


if __name__ == "__main__":
    app.run()
