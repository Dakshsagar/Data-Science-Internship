USE vcet;
create table emp1(
empid int ,
name varchar(50),
country varchar(50));
INSERT into emp1(empid,name,country) VALUES (1,'Shubham',' India');
INSERT into emp1(empid,name,country) VALUES (2,'rahul',' pakistan');
INSERT into emp1(empid,name,country) VALUES (3,'rohan',' colombia');
INSERT into emp1(empid,name,country) VALUES (4,'rohit',' nigeria');
INSERT into emp1(empid,name,country) VALUES (5,'Suryakumar',' usa');

create table emp2(
empid int ,
name varchar(50),
country varchar(50));
INSERT into emp2(empid,name,country) VALUES (1,'Shubham',' brazil');
INSERT into emp2(empid,name,country) VALUES (2,'rahul',' zimbabwe');
INSERT into emp2(empid,name,country) VALUES (3,'rohan',' sri lanka');
INSERT into emp2(empid,name,country) VALUES (4,'rohit',' India');
INSERT into emp2(empid,name,country) VALUES (5,'Suryakumar',' usa');
-- these are set operations to join data in rows
SELECT country from emp1 
union all
SELECT country from emp2
order by country;
-- these are joint operations to join full tables i.e coloumns
create table emp3(
empid int ,
name varchar(50),
country varchar(50));
INSERT into emp3(empid,name,country) VALUES (1,'Shubham',' India');
INSERT into emp3(empid,name,country) VALUES (2,'rahul',' pakistan');
INSERT into emp3(empid,name,country) VALUES (3,'rohan',' colombia');
INSERT into emp3(empid,name,country) VALUES (4,'rohit',' nigeria');
INSERT into emp3(empid,name,country) VALUES (5,'Suryakumar',' usa');

create table emp4(
empid int ,
name varchar(50),
country varchar(50));
INSERT into emp4(empid,name,country) VALUES (1,'Shubham',' brazil');
INSERT into emp4(empid,name,country) VALUES (2,'rahul',' zimbabwe');
INSERT into emp4(empid,name,country) VALUES (8,'rohan',' sri lanka');
INSERT into emp4(empid,name,country) VALUES (7,'rohit',' India');
INSERT into emp4(empid,name,country) VALUES (6,'Suryakumar','italy');
select *
from emp3
inner join emp4
on emp3.empid=emp4.empid ;

create table test_data(
new_id int,
new_cat varchar(50) );
insert into test_data(new_id,new_cat) values(100,'Agni');
insert into test_data(new_id,new_cat) values(200,'Agni');
insert into test_data(new_id,new_cat) values(500,'Dharti');
insert into test_data(new_id,new_cat) values(700,'Dharti');
insert into test_data(new_id,new_cat) values(200,'Vayu');
insert into test_data(new_id,new_cat) values(300,'Vayu');
insert into test_data(new_id,new_cat) values(500,'Vayu');

select new_id, new_cat,
sum(new_id) over( partition by new_cat order by new_id) as "total",
avg(new_id) over( partition by new_cat order by new_id) as "average",
count(new_id) over( partition by new_cat order by new_id) as "count",
min(new_id) over( partition by new_cat order by new_id) as "min",
max(new_id) over( partition by new_cat order by new_id) as "max"
from test_data ;

select new_id, new_cat,
sum(new_id) over( order by new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as "total",
avg(new_id) over( order by new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as "average",
count(new_id) over( order by new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as "count",
min(new_id) over( order by new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as "min",
max(new_id) over( order by new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as "max"
from test_data ;

SELECT new_id, 
row_number() over(order by new_id) as"rownumber",
rank() over(order by new_id) as"rank",
dense_rank() over(order by new_id) as"dense_rank",
percent_rank() over(order by new_id) as"percent_rank"
from test_data;

SELECT new_id, 
first_value(new_id) over(order by new_id) as"first_value",
Last_value(new_id) over(order by new_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING ) as"Last_value",
lead(new_id) over(order by new_id) as"lead",
lag(new_id) over(order by new_id) as"lag"
from test_data;

select new_id,
lead(new_id,2) over(order by new_id) as"lead",
lag(new_id,2) over(order by new_id) as"lag"
from test_data

