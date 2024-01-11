"""
Database:  any collection of related data, like facebook friends, todo list, phone book, etc.
databases can be stored in different ways, like, on computer, on paper, your mind, or spreadsheets.

DBMS: Database Management System, a special software that helps users create and maintain databases.
DBMS does the following:
   * helps manage large amount of information
   * secure
   * backup
   * export and import
   * interacts with other software
   
   
CRUD:
    *Create
    *Read/Retrieve
    *Update
    *Delete

Two types of Databases:
    Relation Databases (SQL): organize data into one or more tables. has column and rows, each row has a unique key
    Non-Relations(NoSQL/ not just SQL): organize data into anything but traditional tables.
      e.g: key-value stores, documents(json,XML,etc),Graphs, Flexible tables

RDBMAS: Relational Database Management Systems: softwares that is used to manage and create relational databases
        e.g: Mysql, oracle, postgreSQL, mariaDB etc.
    
SQL: structed query language, its used to interact with RDBMS.
    * its used to do CRUD operations on RDBMS and other administrative tasks( backup, security, user management, etc.)
    * different RDBMS uses SQL slightly different than the other.
    * sql is 4 languages in one, like DQL,DDL,DML,DCL
    * DQL stands for Data Query Language, which queries database
    * DDL, Data Definition Language, it defingin database schemas, like how many tables or what kind of tables to use
    * DCL, Data Control Language, used for controlling access to the database, user permissions
    * DML, Data Manipulation Language, used to manipulate databases    
NRDBMS: Non-Relations Database Management Systems, helps user create and manage noSQL Databases
        * eg: mongoDB, dynamoDB, apache cassandra, firebase, etc.
        * it does not have a standard language to do crud and other tasks, so you can use your preferred language to do so.
        
Primary Key: unique numbers or identifiers of a row

Surrogat Key: a primary key that has no mapping to the real world, its just a random identifier with no
        special meaning. it does not represent anything, like 200, 201, 203, 300
Natural key: a primary key which also represents a real world number, like passport id, or social security number.
Foreign Key: primary key of another table which is placed into the table to show relationship of the each row
        to the specific rows of the other table
composite Key: two columns which are used as a primary key
    
Queries: set of instructions to retrieve data from the database.        

#now install MYSQL DATABASE, either let it install by default or do custom install, install only MYSQL SERVER, and mysql shell
#either use mysql command line to interact with your database or use an app which connects to your DB 
# and queries it, like POPSQL

Entity is the a table, which may have attributes and derive attributes which is attributes derived from aother one
        