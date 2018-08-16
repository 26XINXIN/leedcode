select 
    Department.Name as Department, 
    Employee.Name as Employee, 
    Employee.Salary as Salary 
from 
    Employee, 
    (
        select max(Salary) as Salary, DepartmentId
        from Employee
        group by DepartmentId
    ) as t1, 
    Department
where 
    Employee.Salary=t1.Salary
    and Employee.DepartmentId=t1.DepartmentId
    and Employee.DepartmentId=Department.Id;