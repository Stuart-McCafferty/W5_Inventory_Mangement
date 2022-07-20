-- Deleting tables before creating again
DROP TABLE IF EXISTS meals_products;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS meals;


CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    link VARCHAR(255),
    phone VARCHAR(255)
);

CREATE TABLE meals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    in_stock BOOLEAN
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    quantity DECIMAL(9,1),
    cost DECIMAL(9,2),
    selling_price DECIMAL(9,2),
    low_stock DECIMAL(9,2),
    supplier_id INT NOT NULL REFERENCES suppliers(id)  ON DELETE CASCADE
);

CREATE TABLE meals_products (
    id SERIAL PRIMARY KEY,
    meal_id INT NOT NULL REFERENCES meals(id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(id) ON DELETE CASCADE
);








