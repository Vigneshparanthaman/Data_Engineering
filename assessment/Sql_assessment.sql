CREATE TABLE Worker (
    WORKER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FIRST_NAME CHAR(25),
    LAST_NAME CHAR(25),
    SALARY INT(15),
    JOINING_DATE DATETIME,
    DEPARTMENT CHAR(25)
);

INSERT INTO Worker
    (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
        (001, 'Monika', 'Arora', 100000, '14-02-20 09.00.00', 'HR'),
        (002, 'Niharika', 'Verma', 80000, '14-06-11 09.00.00', 'Admin'),
        (003, 'Vishal', 'Singhal', 300000, '14-02-20 09.00.00', 'HR'),
        (004, 'Amitabh', 'Singh', 500000, '14-02-20 09.00.00', 'Admin'),
        (005, 'Vivek', 'Bhati', 500000, '14-06-11 09.00.00', 'Admin'),
        (006, 'Vipul', 'Diwan', 200000, '14-06-11 09.00.00', 'Account'),
        (007, 'Satish', 'Kumar', 75000, '14-01-20 09.00.00', 'Account'),
        (008, 'Geetika', 'Chauhan', 90000, '14-04-11 09.00.00', 'Admin');

CREATE TABLE Bonus (
    WORKER_REF_ID INT,
    BONUS_AMOUNT INT(10),
    BONUS_DATE DATETIME,
    FOREIGN KEY (WORKER_REF_ID)
        REFERENCES Worker(WORKER_ID)
        ON DELETE CASCADE
);

INSERT INTO Bonus
    (WORKER_REF_ID, BONUS_AMOUNT, BONUS_DATE) VALUES
        (001, 5000, '16-02-20'),
        (002, 3000, '16-06-11'),
        (003, 4000, '16-02-20'),
        (001, 4500, '16-02-20'),
        (002, 3500, '16-06-11');
   
CREATE TABLE Title (
    WORKER_REF_ID INT,
    WORKER_TITLE CHAR(25),
    AFFECTED_FROM DATETIME,
    FOREIGN KEY (WORKER_REF_ID)
        REFERENCES Worker(WORKER_ID)
        ON DELETE CASCADE
);

INSERT INTO Title
(WORKER_REF_ID, WORKER_TITLE, AFFECTED_FROM) VALUES
 (001, 'Manager', '2016-02-20 00:00:00'),
 (002, 'Executive', '2016-06-11 00:00:00'),
 (008, 'Executive', '2016-06-11 00:00:00'),
 (005, 'Manager', '2016-06-11 00:00:00'),
 (004, 'Asst. Manager', '2016-06-11 00:00:00'),
 (007, 'Executive', '2016-06-11 00:00:00'),
 (006, 'Lead', '2016-06-11 00:00:00'),
 (003, 'Lead', '2016-06-11 00:00:00');


-- Write a query to display all the first_name  in upper case
select upper(FIRST_NAME) from worker;
-- Write a querty to display unique department from workers table
select distinct department from worker;
-- Write an SQL query to print the first three characters of FIRST_NAME from Worker table
select left(FIRST_NAME,3) as First_Name from worker;
-- Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.
select position('a' in 'Amitabh') from worker;
-- Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length
select distinct DEPARTMENT,length(DEPARTMENT) from worker;

-- Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending
select * from worker order by FIRST_NAME asc, DEPARTMENT desc;
-- Write a query to get workers whose name are Vipul and Satish
select * from worker where FIRST_NAME in ('vipul', 'satish');

-- Write an SQL query to print details of the Workers whose FIRST_NAME contains 'a'
select * from worker where FIRST_NAME like "%a%";
-- Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets
select * from worker where FIRST_NAME like "_____h";
-- Write an SQL query to print details of the Workers whose SALARY lies between 100000 and 500000
select * from worker where salary between 100000 and 500000;
-- Write an SQL query to print details of the Workers who have joined in Feb’2014
select * from worker where Joining_date like "%2014-02-%";
-- Write an SQL query to fetch the count of employees working in the department ‘Admin’
select department,count(*) from worker where department = 'Admin';
-- Write an SQL query to fetch the no. of workers for each department in the descending order
select department, count(FIRST_NAME) from worker group by department order by count(FIRST_NAME) desc;
-- Write a query to display workerrs who are managers
select count(*) from Title where WORKER_TITLE = 'manager'; 
select * from Title;
-- Write query to find duplicate rows title table
select worker_title,count(*) from Title group by worker_title having count(*)>1;

-- Write an SQL query to show all workers who got the bonus
-- along with bonus amount

select w.first_name, b.bonus_amount from worker w join bonus b  
on b.worker_ref_id = w.worker_id ;

-- Write a query to find employees in worker table that do not exist in bonus table (ie did not get bonus)
select * from worker;
select w.first_name, b.bonus_amount from worker w left join bonus b  
on b.worker_ref_id = w.worker_id 
where bonus_amount is null;

-- Write a query to find the highest 2 salaries
select distinct salary from worker order by salary desc limit 2;
-- Find 2nd highest without using TOP or LIMIT
select max(salary) as Second_maxsalary from worker
where salary < (
select max(salary) as Second_maxsalary from worker);
-- Find people who have the same salary
select FIRST_NAME,salary from worker where salary = (
select salary from worker group by salary having count(salary) > 1);

-- or 

select * from worker w1
join Worker w2
where w1.salary=w2.salary
and w1.worker_id != w2.worker_id;

-- Write a query to fetch 1st 50% records without using Top
select * from worker;
select count(worker_id) from worker;

-- Write a query to select a department with more than 3 people in worker table
select department from worker group by department having count(department) > 3;

-- Write a query to select 1st and last row of a worker table
(select * from worker order by worker_id asc limit 1)
union all 
(select * from worker order by worker_id desc limit 1);


-- Write a query to select last 5 entries from worker table
select * from worker order by worker_id desc limit 5;
-- Write a query to select people with highest salary in each group
select department,max(salary) from worker group by department;
-- Write a query to fetch departments along with the total salaries paid for each of them
select department,sum(salary) from worker group by department;
-- Write a query to fetch the names of workers who earn the highest salary

select First_name from worker where salary = (
select max(salary) from worker);
