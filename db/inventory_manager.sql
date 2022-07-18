-- Deleting tables before creating again
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;



CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    link VARCHAR(255),
    phone VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    quantity DECIMAL(9,1),
    cost DECIMAL(9,2),
    selling_price DECIMAL(9,2),
    supplier_id INT NOT NULL REFERENCES suppliers(id)  ON DELETE CASCADE
)

