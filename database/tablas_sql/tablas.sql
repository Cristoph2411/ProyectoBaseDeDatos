CREATE TABLE IF NOT EXISTS customer(
    cedula VARCHAR(10) PRIMARY KEY NOT NULL,
    nombre VARCHAR(50),
    whatsapp VARCHAR(20),
    email VARCHAR(50) 
);

CREATE TABLE IF NOT EXISTS orders(
    id SERIAL PRIMARY KEY,
    cedula_cliente VARCHAR(10) REFERENCES customer (cedula),
    cantidad INT NOT NULL,
    metodo_pago VARCHAR(20) NOT NULL,
    observacion VARCHAR(100) NOT NULL,
    ciudad VARCHAR(20) NOT NULL,
    municipio VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    monto_delivery DECIMAL(11,2) NOT NULL,
    total DECIMAL(11,2) NOT NULL,
    capture VARCHAR(50),
    fecha VARCHAR(50) NOT NULL
);