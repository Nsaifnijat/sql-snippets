"""
#create a column with student id as index or primary key
#1 setting primary key method 1
CREATE TABLE student (student_id INT PRIMARY KEY, name VARCHAR(20), major VARCHAR(20));

#2 setting primary key method 2
CREATE TABLE student (student_id INT, name VARCHAR(20), major VARCHAR(20),
PRIMARY KEY(student_id));

#3 use constraints, make name not null, and major unique
CREATE TABLE student (student_id INT, name VARCHAR(20) NOT NULL, major VARCHAR(20) UNIQUE,
PRIMARY KEY(student_id));

# make default, and make id to be added automatically without you putting it
CREATE TABLE student (student_id INT AUTO_INCREMENT, name VARCHAR(20), major VARCHAR(20) DEFAULT 'apps',
PRIMARY KEY(student_id));


#delete table
DROP TABLE student;
# describe the tabel
DESCRIBE TABLE student;

#add another column to the table, GPA in decimals like 000.00
ALTER TABLE student ADD  gpa DECIMAL(3,2);
ALTER TABLE student ADD COLUMN gpa DECIMAL(3,2);

#delete a column
ALTER TABLE student DROP gpa;
ALTER TABLE student DROP COLUMN gpa;

#insert values into your table
INSERT INTO student VALUES(1,'azia','bca',5);
#insert into certain columns
INSERT INTO student (student_id, name) VALUES(2,'WALI');

#update a value
UPDATE student Set major = "BIO" WHERE major = 'bca';
UPDATE student Set major = "BIO" WHERE student_id = 2;
UPDATE student Set name = 'ali', major = "BIO" WHERE student_id = 2;
#set every ones major to chemistry
UPDATE student Set major = 'chemistry';
UPDATE student Set major = "BIO" WHERE major = 'bca' or major = 'chemistry';
#delete all rows
DELETE FROM student;
DELETE FROM student WHERE name = 'ali';
DELETE FROM student WHERE name = 'ali' AND major = 'chemistry';
#quering
#show all data of a table
SELECT * FROM student;
SELECT major from student;
SELECT major FROM student WHERE name = 'ali';
SELECT student.name, student.major FROM student WHERE name = 'ali' ORDER BY name;
# ORDER BY NAME AND DESCENDING
SELECT student.name, student.major FROM student ORDER BY name DESC;
#first order by name and if there is two or more same name then order by major, RETURN ONLY TWO
SELECT student.name, student.major FROM student ORDER BY name, major LIMIT 2;
#select those names which are among these
SELECT * FROM student WHERE name IN ('ALI','JAWID','ZOHAL');
#not equals to
SELECT * FROM student WHERE name <> 'azia';