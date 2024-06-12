
from flask import Flask,request,render_template,jsonify,redirect
app = Flask (__name__)
from psycopg2 import connect,extras

app=Flask(__name__)
#datos para conectarse a la BD
host = 'localhost'
port = 5433
dbname = 'usersDB'
user = 'postgres'
password = '1234'

def get_database():
    conn = connect(host =host,port =port,dbname=dbname,user=user,password=password)
    return conn  
#los decoradores nos permite abrir desde el navegador un archivo especifico
@app.route('/')
def get_users_html():
    return render_template('index.html')

@app.get('/app/users')
def get_users():
    conn = get_database()
    cursor = conn.cursor(cursor_factory = extras.RealDictCursor)
    cursor.execute('select * from users')
    user = cursor.fetchall()
    print(user)
    return jsonify(user)
   
@app.route('/create', methods = ['GET','post'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    if request.method == 'POST':
        username = request.form['username']
        pas = request.form['pass']
        email = request.form['email']

        conn = get_database()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users(username,password,email) VALUES (%s,%s,%s) RETURNING *', (username,pas,email))

        new_created_user = cursor.fetchone()
        print(new_created_user)

        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
@app.route('/<int:id>/delete', methods = ['GET','POST'])
def delete_user(id):
    conn = get_database()
    cursor = conn.cursor(cursor_factory = extras.RealDictCursor)
    cursor.execute('DELETE FROM users where id = %s RETURNING *',(id,))
    user_deleting = cursor.fetchone()
    
    if request.method == 'POST':
        if user_deleting:
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/')
        #abort(404)
    return render_template('delete.html', user=user_deleting)
#asdasdasdasddddddddddddddddd
@app.route('/employees', methods =['GET'])
def get_employees_html():
    conn = get_database()
    cursor = conn.cursor(cursor_factory = extras.RealDictCursor)
    cursor.execute('select * from employees')
    user = cursor.fetchall()
    return render_template('employees.html', users=user)
@app.route('/create/employees', methods = ['GET','post'])
def create_employees():
    if request.method == 'GET':
        return render_template('create_employees.html')
    if request.method == 'POST':
        username = request.form['username']
        pas = request.form['pass']
        email = request.form['email']
        salary = request.form['salary']
        conn = get_database()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO employees(username,password,email,salary) VALUES (%s,%s,%s,%s) RETURNING *', (username,pas,email,salary))

        new_created_user_employees = cursor.fetchone()
        print(new_created_user_employees)

        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/employees')
@app.route('/<int:id>/delete/e', methods = ['GET','POST'])
def delete_user_e(id):
    conn = get_database()
    cursor = conn.cursor(cursor_factory = extras.RealDictCursor)
    cursor.execute('DELETE FROM employees where id = %s RETURNING *',(id,))
    user_deleting_e = cursor.fetchone()
    
    if request.method == 'POST':
        if user_deleting_e:
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/employees')
        #abort(404)
    return render_template('delete_employees.html', user=user_deleting_e)
#sadasdasdasdasdasdasa
    
@app.put('/api/users/1')
def update_user():
    return 'updating users'

@app.get('/api/users/1')
def get_user():
    return 'geting user'

     
     
     
if __name__=='__main__':
    app.run(debug=True)
    
