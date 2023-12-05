SELECT Department.name AS 'Department',
	Employee.name AS 'Employee',
	Salary
FROM Employee JOIN Department ON Employee.departmentId=Department.id
WHERE (Department.id,Salary) IN
	(
	SELECT departmentId,max(salary)
	FROM Employee 
	GROUP BY departmentId
	);