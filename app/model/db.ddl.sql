CREATE DATABASE IF NOT EXISTS libdo;
USE libdo;

CREATE TABLE IF NOT EXISTS plans(
	plan_id  INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(14) NOT NULL,
    favorite BOOLEAN NOT NULL,
    cost FLOAT NOT NULL,
    premium BOOLEAN NOT NULL,
    points VARCHAR(150) NOT NULL
);

CREATE TABLE IF NOT EXISTS users(
	user_id BIGINT PRIMARY KEY,
    email VARCHAR(64) NOT NULL,
    name VARCHAR(24) NOT NULL,
    surname VARCHAR(24) NOT NULL,
    bio VARCHAR(200),
    recovery_token VARCHAR(16),
    country_code VARCHAR(4) NOT NULL,
    city VARCHAR(14) NOT NULL,
    plan_id INT NOT NULL,
    paypal_email VARCHAR(64) NOT NULL,
    image_path TEXT NOT NULL,
    password VARCHAR(64) NOT NULL,
    library_name VARCHAR(24) NOT NULL,
    created_on DATE NOT NULL,
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id)
);

CREATE TABLE IF NOT EXISTS types(
	type_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(24) NOT NULL
);

CREATE TABLE IF NOT EXISTS products(
	product_id INT PRIMARY KEY AUTO_INCREMENT,
	user_id BIGINT NOT NULL,
	file_path VARCHAR(80) NOT NULL,
	hidden BOOLEAN NOT NULL,
    title VARCHAR(64) NOT NULL,
    description VARCHAR(100) NOT NULL,
    type_id INT NOT NULL,
  	cost INT NOT NULL,
  	FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (type_id) REFERENCES types(type_id)
);


CREATE TABLE IF NOT EXISTS reviews(
	review_id INT PRIMARY KEY AUTO_INCREMENT,
    stars INT NOT NULL,
    created_on DATE NOT NULL,
    content VARCHAR(200) NOT NULL,
    user_id BIGINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS orders(
	order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT,
    tk VARCHAR(50),
    created_on DATETIME NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE IF NOT EXISTS reviews(
	review_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    content VARCHAR(200) NOT NULL,
    created_on DATETIME NOT NULL,
    stars INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);