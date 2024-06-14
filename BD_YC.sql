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
