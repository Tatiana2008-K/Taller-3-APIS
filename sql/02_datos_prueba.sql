USE tienda_adso;
---Ejecuta solo una vez, para evitar duplicados
INSERT INTO clientes (nombre, correo) VALUES ('Ana Pérez', 'ana@example.com'), ('Carlos Ruiz', 'carlos@example.com');
INSERT INTO productos (nombre, precio, stock) VALUES ('Mouse', 35000, 20), ('Teclado', 80000, 7), ('Monitor', 650000, 4);
