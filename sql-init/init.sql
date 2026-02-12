CREATE TABLE customer (
    type VARCHAR(20),
    customerNumber INT(20) PRIMARY KEY,
    customerName VARCHAR(100),
    contactLastName VARCHAR(100),
    contactFirstName VARCHAR(100),
    phone VARCHAR(50),
    addressLine1 VARCHAR(100),
    addressLine2 VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    postalCode VARCHAR(100),
    country VARCHAR(100),
    salesRepEmployeeNumber INT(20),
    creditLimit float(100),
);


CREATE TABLE order (
    type VARCHAR(20) ,
    orderNumber INT(20) PRIMARY KEY,
    orderDate VARCHAR(100),
    requiredDate VARCHAR(100),
    shippedDate VARCHAR(100),
    status VARCHAR(100),
    comments VARCHAR(100),
    customerNumber INT(20),
    FOREIGN KEY (customerNumber) REFERENCES customer(customerNumber)
);



