SHOW DATABASES;


CREATE TABLE USERS (
    id int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE DRIVERS (
    id int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE ORDERS (
    id int PRIMARY KEY AUTO_INCREMENT,
    user_id int,
    driver_id int,
    order_datetime DATETIME,
    FOREIGN KEY (USER_ID) REFERENCES USERS(ID),
    FOREIGN KEY (DRIVER_ID) REFERENCES DRIVERS(ID)
);

SHOW TABLES;


INSERT INTO USERS (name, phone) VALUES ('John Doe', '123-456-7890'),
                                       ('Jane Smith', '987-654-3210'),
                                       ('Alice Johnson', NULL),
                                       ('Robert William Anderson', '555-1234');

INSERT INTO DRIVERS (name, phone) VALUES ('Michael Johnson', '555-1111'),
                                       ('Emily Davis', '777-2222'),
                                       ('David Smith', NULL),
                                       ('Sarah Brown', '888-3333');

INSERT INTO ORDERS (user_id, driver_id, order_datetime) VALUES (1, 1, '2024-01-13 10:30:00'),
                                                               (2, 2, '2024-01-13 11:45:00'),
                                                               (3, 3, '2024-01-13 13:15:00'),
                                                               (1, 4, '2024-01-13 15:00:00');


SELECT *
FROM USERS;

SELECT *
FROM DRIVERS;

SELECT *
FROM ORDERS;