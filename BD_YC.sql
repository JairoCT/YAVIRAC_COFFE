CREATE TABLE productos(
id serial primary key,
stock integer,
nombre_product VARCHAR (25),
precio_product decimal
);

INSERT INTO productos (stock,nombre_product,precio_product) VALUES (20, 'Expresso' , 2.00);
INSERT INTO productos (stock,nombre_product,precio_product) VALUES (30, 'Americano' , 4.00);
INSERT INTO productos (stock,nombre_product,precio_product) VALUES (40, 'Café con leche' , 3.00);
INSERT INTO productos (stock,nombre_product,precio_product) VALUES (50, 'Capuchino' , 4.50);




CREATE TABLE rol(
	id_rol INT primary key,
	nombre_rol varchar (50),
	);

CREATE TABLE usuario(
    id_usuario INT primary key,
    cedula integer,
    nombre VARCHAR (50),
    apellido VARCHAR (50),
    correo_electronico VARCHAR (50),
    contraseña VARCHAR (50),
    direccion VARCHAR (50),
    telefono integer ,
    fecha_nacimiento date
    id_rol INT,
    FOREIGN KEY (id_rol) REFERENCES rol(id_rol));

CREATE TABLE Pedidos(
	id serial primary key,
	Cantidad integer,
	Fecha_pedido date,
	Subtotal integer,
	Iva_Incluido integer,
	Total_todo integer);


CREATE TABLE Carrito(
	id serial primary key,
    Productos varchar(50),
	Cantidad integer,
	Precio decimal,
	Total integer);


CREATE TABLE Categoria(
    id serial primary key,
    Nombre_Categ varchar(50)
);