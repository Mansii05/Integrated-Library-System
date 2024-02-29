create database lms;
show databases;
create table Books(book_id varchar(255),book_name varchar(255),author_name varchar(255),primary key(book_id));
select * from books;
insert into books values("b001","Learning Python","Reema Theraja");
insert into books values("b005","SQL Fundamentals","Ashish Gupta");
insert into books values("b007","Basics of Power Bi","Pawan Das");
create table student(student_id varchar (255),s_password varchar(255),primary key (student_id));
select * from student;
insert into student values("mansi001@gmail.com","1234");
insert into student values("vickyMaan@gmail.com","1002");
insert into student values("JammyLever@gmail.com","5678");
create table admin(librarian_id varchar(255),l_password varchar(255),primary key(librarian_id));
select * from admin;
insert into admin values("rajesh_librarian@gmail.com","lib005");
insert into admin values("pankaj_librarian@gmail.com","lib008");
insert into admin values("sudhanshu_librarian@gmail.com","lib006");
create table issues(issue_id varchar(255),bookid varchar(255),studentid varchar(255));
select * from issues;
insert into issues values("i001","b005","JammyLever@gmail.com");
insert into issues values("i002","b001","mansi001@gmail.com");
insert into issues values("i002","b007","vickyMaan@gmail.com");


