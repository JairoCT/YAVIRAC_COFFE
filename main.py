
from flask import Flask,request,render_template,redirect
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
@app.route('/registro', methods = ['GET','POST'])
def registro():
    if request.method == 'GET':
        return render_template('Registro.html')
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo_electronico = request.form['correo_electronico']
        contraseña = request.form['contraseña']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        fecha_nacimiento = request.form['fecha_nacimiento']

        conn = get_database()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuario(cedula,nombre,apellido,correo_electronico,contraseña,direccion,telefono,fecha_nacimiento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *', (cedula,nombre,apellido,correo_electronico,contraseña,direccion,telefono,fecha_nacimiento))

        new_user = cursor.fetchone()
        print(new_user)

        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
#RUTAS ADMINITRADOR
@app.route('/admin')
def indx_admin():
    return render_template('index_admin.html')
@app.route('/productos_admin')
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
        return redirect('/productos_admin')
    
    return render_template('edit_productos.html', producto=producto)
@app.route('/create', methods = ['GET','POST'])
def create_producto():
    if request.method == 'GET':
        return render_template('agregar_productos_admin.html')
    if request.method == 'POST':
        stock = request.form['stock']
        nombre_product = request.form['nombre_product']
        precio_product = request.form['precio_product']

        conn = get_database()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO productos(stock,nombre_product,precio_product) VALUES (%s,%s,%s) RETURNING *', (stock,nombre_product,precio_product))

        new_product = cursor.fetchone()
        print(new_product)

        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/productos_admin')
@app.route('/<int:id>/delete', methods = ['GET','POST'])
def delete_producto(id):
    conn = get_database()
    cursor = conn.cursor(cursor_factory = extras.RealDictCursor)
    cursor.execute('DELETE FROM productos where id = %s RETURNING *',(id,))
    productos = cursor.fetchone()
    
    if request.method == 'POST':
        if productos:
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/productos_admin')
        #abort(404)
    return render_template('delete_producto_admin.html', producto=productos)  

@app.route('/<int:id>/edit/usuarios', methods=['GET', 'POST'])
def edit_correo(id):
    conn = get_database()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute('SELECT * FROM usuario WHERE id = %s', (id,))
    usuario = cursor.fetchone()
    
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo_electronico = request.form['correo_electronico']
        contraseña = request.form['contraseña']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        fecha_nacimiento = request.form['fecha_nacimiento']
        # Actualiza la información del producto en la base de datos
        cursor.execute('UPDATE usuario SET cedula = %s, nombre = %s, apellido = %s, correo_electronico = %s, contraseña = %s, direccion = %s, telefono = %s, fecha_nacimiento = %s WHERE id = %s', 
                       (cedula, nombre, apellido, correo_electronico, contraseña, direccion, telefono, fecha_nacimiento,id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/usuarios_admin')
    
    return render_template('edit_usuarios.html', usuario=usuario)
@app.route('/<int:id>/delete/usuarios', methods = ['GET','POST'])
def delete_usuarios(id):
    conn = get_database()
    cursor = conn.cursor(cursor_factory = extras.RealDictCursor)
    cursor.execute('DELETE FROM usuario where id = %s RETURNING *',(id,))
    usuarios = cursor.fetchone()
    
    if request.method == 'POST':
        if usuarios:
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/usuarios_admin')
        #abort(404)
    return render_template('delete_usuarios.html', usuarios=usuarios)  
@app.route('/usuarios_admin')
def usuarios_admin():
    conn = get_database()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute('SELECT * FROM usuario')
    usuarios = cursor.fetchall()
    return render_template('usuarios_admin.html', usuarios=usuarios)







if __name__=='__main__':
    app.run(debug=True)
    
