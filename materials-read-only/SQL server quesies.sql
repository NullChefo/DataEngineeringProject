CREATE TABLE USERS_MAXIM (
    userid int PRIMARY KEY IDENTITY,
    username VARCHAR(100),
    userphone VARCHAR(20)
);

CREATE TABLE DRIVERS_MAXIM (
    driverid int PRIMARY KEY IDENTITY,
    drivername VARCHAR(100),
    driverphone VARCHAR(20)
);

CREATE TABLE ORDERS_MAXIM (
    orderid int PRIMARY KEY IDENTITY,
    orderuserid int,
    orderdriverid int,
    orderdatetime DATETIME,
    FOREIGN KEY (orderuserid) REFERENCES USERS_MAXIM(userid),
    FOREIGN KEY (orderdriverid) REFERENCES DRIVERS_MAXIM(driverid)
);


-- Inserts for USERS_MAXIM table
INSERT INTO USERS_MAXIM (username, userphone) VALUES ('John Doe', '123-456-7890'),
                                                    ('Jane Smith', '987-654-3210'),
                                                    ('Alice Johnson', '555-1234'),
                                                    ('Robert Anderson', '111-222-3333');

-- Inserts for DRIVERS_MAXIM table
INSERT INTO DRIVERS_MAXIM (drivername, driverphone) VALUES ('Michael Johnson', '555-1111'),
                                                          ('Emily Davis', '777-2222'),
                                                          ('David Smith', '888-3333'),
                                                          ('Sarah Brown', '999-4444');

-- Inserts for ORDERS_MAXIM table
INSERT INTO ORDERS_MAXIM (orderuserid, orderdriverid, orderdatetime) VALUES (1, 1, '2024-01-13 10:30:00'),
                                                                            (2, 2, '2024-01-13 11:45:00'),
                                                                            (3, 3, '2024-01-13 13:15:00'),
                                                                            (1, 4, '2024-01-13 15:00:00');
