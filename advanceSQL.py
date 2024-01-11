CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    birthday DATE,
    sex VARCHAR(1),
    salary INT,
    super_id INT,
    branch_id INT
);
#super_id and branch_id should be foreign key since right the tables for the foreign key is not created, we cannot make them foreign
CREATE TABLE branch (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(40),
    mgr_id INT,
    mgr_start_date DATE,
    FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

#NOW we can set the branch id and super id of employee as foreign keys
ALTER TABLE employee ADD FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL;
ALTER TABLE employee ADD FOREIGN KEY(super_id) REFERENCES employee(emp_id) ON DELETE SET NULL;

CREATE TABLE client(
    client_id INT PRIMARY KEY,
    client_name VARCHAR(40),
    branch_id INT,
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);

#now we create a table with composite primary key
CREATE TABLE works_with (
    emp_id INT,
    client_id INT,
    total_sales INT,
    PRIMARY KEY(emp_id,client_id),
    FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE  CASCADE,
    FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE  CASCADE
);

CREATE TABLE branch_supplier(
    branch_id INT,
    supplier_name VARCHAR(40),
    supply_type VARCHAR(40),
    PRIMARY KEY(branch_id, supplier_name),
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);

#populate the tables
INSERT INTO employee VALUES(100, 'David', 'Wallace', '1967-11-30','M', 25000, NULL,NULL);
INSERT INTO branch VALUES(1, 'corporate', 100, '2006-5-14');
UPDATE employee SET branch_id = 1 WHERE emp_id = 100;
INSERT INTO employee VALUES(101, 'John', 'Wallace', '1969-11-30','M', 28000, 100,1);
#DELETE  FROM employee where emp_id = 1001;
#scranto branch
INSERT INTO employee VALUES(102, 'Jan', 'Wallace', '1960-11-30','M', 5000, NULL,NULL);
INSERT INTO branch VALUES(2, 'scranton', 102, '2006-5-14');
UPDATE employee SET branch_id = 2 WHERE emp_id = 102;
INSERT INTO employee VALUES(103, 'josh', 'jang', '1969-11-30','M', 28000, 102,2);
INSERT INTO employee VALUES(104, 'joe', 'david', '1965-11-30','M', 24000, 102,2);
INSERT INTO employee VALUES(105, 'jack', 'doe', '1963-11-30','M', 2000, 102,2);

#stanford branch employee and managers
INSERT INTO employee VALUES(106, 'Jeff', 'ali', '1970-11-30','M', 55500, NULL,NULL);
INSERT INTO branch VALUES(3, 'stanford', 106, '2009-5-14');
UPDATE employee SET branch_id = 3 WHERE emp_id = 106;
INSERT INTO employee VALUES(107, 'jackson', 'khan', '1968-11-30','F', 9000, 106,3);
INSERT INTO employee VALUES(108, 'saif', 'jawid', '1990-11-30','M', 24000, 106,3);

#supplier table
INSERT INTO branch_supplier VALUES(2,'hammer mil','paper');
INSERT INTO branch_supplier VALUES (2, 'notepad', 'office supplies');
INSERT INTO branch_supplier VALUES (3, 'wrench set', 'tools');
INSERT INTO branch_supplier VALUES (2, 'screws', 'hardware');
INSERT INTO branch_supplier VALUES(3, 'screwdriver set', 'tools');
INSERT INTO branch_supplier VALUES(2, 'sticky notes', 'office supplies');
INSERT INTO branch_supplier VALUES(2, 'paintbrushes', 'art supplies');

#client
INSERT INTO client VALUES(400, 'dunmore high school', 2);
INSERT INTO client VALUES(401, 'hometown bank', 3);
INSERT INTO client VALUES(402, 'sunrise medical center', 1);
INSERT INTO client VALUES(403, 'pine grove elementary', 3);
INSERT INTO client VALUES(404, 'valley community college', 2);
INSERT INTO client VALUES(405, 'oakridge retirement home', 1);
#works with
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(106, 401, 60000);
INSERT INTO works_with VALUES(107, 402, 65000);
INSERT INTO works_with VALUES(108, 403, 70000);
INSERT INTO works_with VALUES(109, 404, 75000);
INSERT INTO works_with VALUES(110, 405, 80000);


#THE ABOVE WAS OUR DATABASE SCHEMA FOR THIS COMPANY
#LETS QUERY THE ABOVE DATABASE, renaming our columns when returning them or using Alias,
SELECT first_name AS forename, last_name as finalName FROM employee;
#find all different genders or branches
SELECT DISTINCT sex FROM employee;
#count employees
SELECT COUNT(emp_id) FROM employee;
#show average salary of Males
SELECT AVG(salary) FROM employee WHERE sex = 'M';
#SUM OF ALL MONEY PAID TO EMPLOYEE
SELECT SUM(salary) FROM employee;
SELECT COUNT(sex), sex FROM employee GROUP BY sex;
#how much each employee sold
SELECT SUM(total_sales), emp_id FROM works_with GROUP BY emp_id;
#how much each client spent
SELECT SUM(total_sales), client_id FROM works_with GROUP BY client_id;

#wildcards, when it ends with b, anywhere '%b%', _ is one char, for more go to https://www.w3schools.com/sql/sql_wildcards.asp
SELECT * FROM client WHERE client_name LIKE '%b';

#union combines two queries into one result, UNION ALL returns duplicates too
SELECT City FROM Customers
UNION 
SELECT City FROM Suppliers
ORDER BY City;

#joins, JOIN, LEFT JOIN, RIGHT JOIN, INNER JOIN
SELECT employee.emp_id, employee.first_name, branch.branch_id FROM employee
JOIN branch
ON employee.emp_id = branch.mgr_id;

#nested queries
SELECT employee.first_name, employee.last_name 
FROM employee
WHERE employee.emp_id IN (
    SELECT works_with.emp_id FROM works_with WHERE works_with.total_sales > 3000
);

#trigger table
CREATE TABLE triggerTest (
    message VARCHAR(50)
);
#triggers, are used for logging, and they should be written in mysql command line
#first we need to change delimiter from ; to $$
DELIMITER $$;
#choose database using below command
#use saifnijat
CREATE
    TRIGGER mytrigger BEFORE INSERT ON
    employee
    FOR EACH ROW BEGIN
        INSERT INTO triggerTest VALUES('added new employee');
    END$$
#change delimter back to its main, ;
#DELIMITER ; 
DROP TRIGGER triggerTest;
SELECT * FROM triggerTest;
#TRIGGERS LINK,https://www.giraffeacademy.com/databases/sql/triggers/

#ER DIAGRAM is the schema of a database, go to this link for learning about ER DIAGRAM,https://www.giraffeacademy.com/databases/sql/er-diagrams-intro/