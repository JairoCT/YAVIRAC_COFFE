
from flask import Flask,request,render_template,jsonify,redirect
app = Flask (__name__)
from psycopg2 import connect,extras

app=Flask(__name__)
# datos para conectarse a la BD
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
def inicio():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('Productos.html')
   
@app.route('/carrito')
def carrito():
    return render_template('miCarrito.html')

@app.route('/registro')
def registro():
    return render_template('Registro.html')  
     
if __name__=='__main__':
    app.run(debug=True)
    
