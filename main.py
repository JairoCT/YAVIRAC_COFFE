
from flask import Flask,request,render_template,jsonify,redirect
app = Flask (__name__)
from psycopg2 import connect,extras

app=Flask(__name__)
# datos para conectarse a la BD
host = 'localhost'
port = 5432
dbname = 'BD_YC'
user = 'postgres'
password = '6822'

def get_database():
    conn = connect(host =host,port =port,dbname=dbname,user=user,password=password)
    return conn  
#los decoradores nos permite abrir desde el navegador un archivo especifico
@app.route('/')
def inicio():
    return render_template('index.html')
@app.route('/productos', methods=['GET'])
def productos():
    conn = get_database()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    return render_template('Productos.html', productos=productos)
@app.route('/carrito')
def carrito():
    return render_template('miCarrito.html')

@app.route('/registro')
def registro():
    return render_template('Registro.html')  
     

#RUTAS ADMINITRADOR
@app.route('/Productos_admin')
def Productos_admin():
    conn = get_database()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    return render_template('Productos_admin.html', productos=productos)


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    conn = get_database()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute('SELECT * FROM productos WHERE id = %s', (id,))
    producto = cursor.fetchone()
    
    if request.method == 'POST':
        stock = request.form['stock']
        nombre_product = request.form['nombre_product']
        precio_product = request.form['precio_product']
        # Actualiza la información del producto en la base de datos
        cursor.execute('UPDATE productos SET stock = %s, nombre_product = %s, precio_product = %s WHERE id = %s', 
                       (stock, nombre_product, precio_product, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/Productos_admin')
    
    return render_template('edit_productos.html', producto=producto)


if __name__=='__main__':
    app.run(debug=True)
    
