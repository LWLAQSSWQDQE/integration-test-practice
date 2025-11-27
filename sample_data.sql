#数据库测试数据
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO users (name,email) VALUES ("Bob","bob@example.com");
INSERT INTO users (name,email) VALUES ("Charlie","charlie@example.com");
