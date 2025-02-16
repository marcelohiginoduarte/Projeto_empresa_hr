
CREATE TABLE customer
(
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    joined_at timestamp NOT NULL
);

CREATE TABLE customer_order
(
    customer_order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    amount INT NOT NULL,
    order_date timestamp NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE
);


CREATE TABLE product
(
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE stock
(
    stock_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES product(product_id) ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(product_id) ON UPDATE CASCADE
);

CREATE TABLE order_item
(
    order_item_id SERIAL PRIMARY KEY,
    customer_order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (customer_order_id) REFERENCES customer_order(customer_order_id) ON UPDATE CASCADE, 
    FOREIGN KEY (product_id) REFERENCES product(product_id) ON UPDATE CASCADE
);


-- current date
insert into customer (name, email, joined_at) VALUES('marcus', 'marcus@gmail.com', current_timestamp);
insert into customer (name, email, joined_at) VALUES('davi', 'davi@gmail.com', current_timestamp);
insert into customer (name, email, joined_at) VALUES('daniel', 'daniel@gmail.com', current_timestamp);
insert into customer (name, email, joined_at) VALUES('camila', 'camila@gmail.com', current_timestamp);
insert into customer (name, email, joined_at) VALUES('paulo', 'paulo@gmail.com', current_timestamp);
insert into customer (name, email, joined_at) VALUES('paula', 'paula@gmail.com', current_timestamp);

-- custom date
insert into customer (name, email, joined_at) VALUES('caio', 'caio@gmail.com', '2020-10-01 14:01:10-08');
insert into customer (name, email, joined_at) VALUES('pedro', 'pedro@gmail.com', '2020-10-05 14:01:10-08');
insert into customer (name, email, joined_at) VALUES('vinicius', 'vinicius@gmail.com', '2020-10-15 14:01:10-08');
insert into customer (name, email, joined_at) VALUES('larissa', 'larissa@gmail.com', '2020-11-05 14:01:10-08');
insert into customer (name, email, joined_at) VALUES('rafael', 'rafael@gmail.com', '2020-11-09 14:01:10-08');
insert into customer (name, email, joined_at) VALUES('icaro', 'icaro@gmail.com', '2020-11-12 14:01:10-08');

-- customer_order
insert into customer_order (amount, order_date, customer_id) VALUES(10, current_timestamp, 1);
insert into customer_order (amount, order_date, customer_id) VALUES(10, current_timestamp, 1);
insert into customer_order (amount, order_date, customer_id) VALUES(10, current_timestamp, 2);
insert into customer_order (amount, order_date, customer_id) VALUES(10, current_timestamp, 3);
insert into customer_order (amount, order_date, customer_id) VALUES(10, current_timestamp, 3);
insert into customer_order (amount, order_date, customer_id) VALUES(10, current_timestamp, 1);
insert into customer_order (amount, order_date, customer_id) VALUES(10, current_timestamp, 4);

-- customer_order with custom_date
insert into customer_order (amount, order_date, customer_id) VALUES(10, '2020-10-02 14:20:10-08', 5);
insert into customer_order (amount, order_date, customer_id) VALUES(10, '2020-10-03 14:23:10-08', 6);
insert into customer_order (amount, order_date, customer_id) VALUES(10, '2020-10-04 14:55:10-08', 7);
insert into customer_order (amount, order_date, customer_id) VALUES(10, '2020-10-05 14:44:10-08', 7);
insert into customer_order (amount, order_date, customer_id) VALUES(10, '2020-10-06 14:33:10-08', 8);
insert into customer_order (amount, order_date, customer_id) VALUES(10, '2020-10-07 14:22:10-08', 6);
insert into customer_order (amount, order_date, customer_id) VALUES(10, '2020-10-08 14:11:10-08', 5);

-- products
insert into product (name) VALUES('e-book');
insert into product (name) VALUES('book');
insert into product (name) VALUES('audio book');

-- stocks
insert into stock (product_id, quantity) VALUES(1, 50);
insert into stock (product_id, quantity) VALUES(1, 30);
insert into stock (product_id, quantity) VALUES(1, 40);

-- order_item
insert into order_item (customer_order_id, product_id, quantity) VALUES(1, 1, 1);
insert into order_item (customer_order_id, product_id, quantity) VALUES(2, 2, 1);
insert into order_item (customer_order_id, product_id, quantity) VALUES(3, 3, 1);
insert into order_item (customer_order_id, product_id, quantity) VALUES(4, 1, 1);
insert into order_item (customer_order_id, product_id, quantity) VALUES(5, 2, 1);
insert into order_item (customer_order_id, product_id, quantity) VALUES(6, 3, 1);
insert into order_item (customer_order_id, product_id, quantity) VALUES(7, 1, 1);
insert into order_item (customer_order_id, product_id, quantity) VALUES(8, 2, 1);
insert into order_item (customer_order_id, product_id, quantity) VALUES(9, 3, 1);


postgres=# SELECT COUNT(*) FROM customer;
 count
-------
    12
(1 row)


postgres=# SELECT COUNT(DISTINCT c.customer_id)
postgres-# FROM customer c
postgres-# LEFT JOIN customer_order o ON c.customer_id = o.customer_id
postgres-# LEFT JOIN order_item oi ON o.customer_order_id = oi.customer_order_id
postgres-# WHERE oi.customer_order_id IS NULL;
 count
-------
     8
(1 row)


postgres=# SELECT p.product_id, p.name, SUM(oi.quantity) AS total_vendido
postgres-# FROM order_item oi
postgres-# JOIN product p ON oi.product_id = p.product_id
postgres-# GROUP BY p.product_id, p.name
postgres-# ORDER BY total_vendido DESC
postgres-# LIMIT 1;
 product_id | name | total_vendido
------------+------+---------------
          2 | book |             3
(1 row)