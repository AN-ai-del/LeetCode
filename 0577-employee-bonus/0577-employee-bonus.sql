# Write your MySQL query statement below
SELECT Employee.name, Bonus.bonus
FROM Bonus
RIGHT JOIN Employee ON Bonus.empId=Employee.empId
WHERE bonus IS NULL OR bonus<1000
ORDER BY Employee.empId;