-- create
-- Create the EMPLOYEE table
CREATE TABLE EMPLOYEE (
  empId INT,
  name VARCHAR(15),
  dept VARCHAR(10)
);

-- Insert data into EMPLOYEE table
INSERT INTO EMPLOYEE(empId, name, dept) VALUES (1, 'Clark', 'Sales');
INSERT INTO EMPLOYEE(empId, name, dept) VALUES (2, 'Dave', 'Accounting');
INSERT INTO EMPLOYEE(empId, name, dept) VALUES (3, 'Ava', 'Sales');

-- Create temporary table for employee details
CREATE TABLE #EmpDetails (
  id INT,
  name VARCHAR(25)
);

-- Insert data into temporary table
INSERT INTO #EmpDetails VALUES (01, 'lalit'), (02, 'atharva');

-- View data from temporary table
SELECT * FROM #EmpDetails;

-- Create the details table
CREATE TABLE details (
  name VARCHAR(30),
  city VARCHAR(30),
  salary INT
);

-- Insert data into details table
INSERT INTO details(name, city, salary) VALUES('abc', 'delhi', 20000);
INSERT INTO details(name, city, salary) VALUES('def', 'mumbai', 23500);
INSERT INTO details(name, city, salary) VALUES('ghi', 'delhi', 26700);
INSERT INTO details(name, city, salary) VALUES('jkl', 'kolkata', 28000);
INSERT INTO details(name, city, salary) VALUES('hadha', 'chennai', 12000);

-- View data from details table
SELECT * FROM details;

-- Query to select data from details table within a salary range
SELECT * FROM details WHERE salary BETWEEN 20000 AND 25000;

-- Create the details1 table with customer details
CREATE TABLE details1 (
  customerid INT,
  firstname VARCHAR(30),
  lastname VARCHAR(30),
  city VARCHAR(30),
  state VARCHAR(30)
);

-- Insert data into details1 table
INSERT INTO details1(customerid, firstname, lastname, city, state) VALUES(678, 'John', 'Doe', 'mumbai', 'MH');
INSERT INTO details1(customerid, firstname, lastname, city, state) VALUES(223, 'Jane', 'Smith', 'delhi', 'NCR');
INSERT INTO details1(customerid, firstname, lastname, city, state) VALUES(345, 'Alice', 'Johnson', 'mumbai', 'MH');
INSERT INTO details1(customerid, firstname, lastname, city, state) VALUES(234, 'Bob', 'Williams', 'kolkata', 'WB');
INSERT INTO details1(customerid, firstname, lastname, city, state) VALUES(212, 'Emily', 'Brown', 'pune', 'MH');

-- data from details1 table
SELECT * FROM details1;

-- Query to order data by customer ID in table
SELECT * FROM details1 ORDER BY customerid;

--group by clause 
SELECT state, COUNT(*) as Total_Customers FROM details1 GROUP BY state;
-- Query to group data by state in details1
SELECT state, COUNT(*) as Total_Customers 
FROM details1 
GROUP BY state 
HAVING COUNT(*) >= 1;

CREATE TABLE payment (
  id INT,
  amount INT,
  mode varchar(30),
  paymentdate varchar(30)
);

INSERT into payment(id,amount,mode,paymentdate) VALUES(1,60,'cash','28/12/24')
INSERT into payment(id,amount,mode,paymentdate) VALUES(2,90,'debit card','24/10/24')
INSERT into payment(id,amount,mode,paymentdate) VALUES(3,120,'cash','24/06/24')
INSERT into payment(id,amount,mode,paymentdate) VALUES(4,100,'credit card','22/12/24')
INSERT into payment(id,amount,mode,paymentdate) VALUES(5,120,'cash','10/12/24')
SELECT mode,sum(amount) as Total
from payment
group by mode
HAVING sum(amount)>=70


create TABLE infotable(
employeid int,
name varchar(30),
gender varchar(2),
department varchar(20),
education varchar(10),
month varchar(20),
salary int);
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1001, 'avi','M','Engineering','UG','january',45)
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1002, 'alok','M','HR','PG','january',28)
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1003, 'chandan','M','sales','UG','january',32)
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1004, 'vandan','M','Sales','UG','Februrary',12)
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1005, 'piyush','M','Marketing','UG','january',69)
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1006, 'sneha','F','Engineering','UG','march',20)
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1007, 'bablu','M','Engineering','PG','january',45)
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1008, 'babli','F','Admin','PG','january',40)
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1009, 'elvish','M','Admin','UG','march',71)
INSERT into infotable(employeid, name,gender, department, education,month, salary) VALUES (1010, 'carrie','F','HIgh School','high school','april',30)

SELECT * FROM infotable
SELECT * FROM infotable WHERE salary >=20 AND education != 'UG';
SELECT department,sum(salary) as Total
FROM infotable
group by department
having sum(salary)>= 30