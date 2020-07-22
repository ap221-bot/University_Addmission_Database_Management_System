mysql> create table admins(
    -> admin_id char(100) not null,
    -> password char(100) not null,
    -> email char(100) not null,
    -> primary key(admin_id));
Query OK, 0 rows affected (0.25 sec)

mysql> create table students(
    -> student_id char(100) not null,
    -> password char(100) not null,
    -> email char(100) not null,
    -> primary key(student_id));
Query OK, 0 rows affected (0.72 sec)

mysql> create table STDB(
    -> app_id int(100) not null,
    -> 
    -> name C^C^C

^C
mysql> create table STDB(
    -> app_id int(100) not null,
    -> name char(100) not null,
    -> email char(100) not null,
    -> gender char(100) not null,
    -> contact char(100) not null,
    -> dob char(100) not null,
    -> Address char(100) not null,
    -> student_id char(100) not null,
    -> primary key(app_id),
    -> FOREIGN KEY (student_id) REFERENCES students(student_id));
Query OK, 0 rows affected (1.58 sec)

mysql> create table preference(
    -> app_id int(100) not null,
    -> pref1 char(100) not null,
    -> pref2 char(100) not null,
    -> pref3 char(100) not null);
Query OK, 0 rows affected (0.36 sec)

mysql> create table qualification(
    -> app_id int(100) not null,
    -> type char(100) not null,
    -> rank char(100) not null,
    -> marks char(100) not null,
    -> foreign key (app_id) references STDB(app_id));
Query OK, 0 rows affected (0.37 sec)

mysql> alter table preference add foreign key (app_id) references STDB(app_id);  
Query OK, 0 rows affected (0.72 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc preference;
+--------+-----------+------+-----+---------+-------+
| Field  | Type      | Null | Key | Default | Extra |
+--------+-----------+------+-----+---------+-------+
| app_id | int(100)  | NO   | MUL | NULL    |       |
| pref1  | char(100) | NO   |     | NULL    |       |
| pref2  | char(100) | NO   |     | NULL    |       |
| pref3  | char(100) | NO   |     | NULL    |       |
+--------+-----------+------+-----+---------+-------+
4 rows in set (0.00 sec)


