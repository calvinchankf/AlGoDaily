-- 1st: select from 2 tables
SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id AND a.Salary > b.Salary;

-- 2nd: JOIN
SELECT
     a.NAME AS Employee
FROM Employee AS a 
JOIN Employee AS b
    ON a.ManagerId = b.Id
    AND a.Salary > b.Salary;