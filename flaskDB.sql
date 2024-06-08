SELECT * FROM flask_db.users;
SELECT * FROM flask_db.products;
SELECT * FROM flask_db.categories;
SELECT * FROM flask_db.orders;
SELECT * FROM flask_db.order_items;
ALTER TABLE users MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE users DROP COLUMN role;
ALTER TABLE users DROP COLUMN password;
ALTER TABLE users RENAME TO customers;

ALTER TABLE order_items
MODIFY unit_price float;
ALTER TABLE products
MODIFY COLUMN price float;
ALTER TABLE orders
MODIFY COLUMN order_date varchar(30);
ALTER TABLE orders
MODIFY COLUMN total_amount float;




CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    stock_quantity INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATETIME,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES users(id)
);

CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

