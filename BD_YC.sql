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


CREATE TABLE usuario(
id serial primary key,
cedula integer,
nombre VARCHAR (50),
apellido VARCHAR (50),
correo_electronico VARCHAR (50),
contraseña VARCHAR (50),
direccion VARCHAR (50),
telefono integer ,
fecha_nacimiento date);

select * from usuario