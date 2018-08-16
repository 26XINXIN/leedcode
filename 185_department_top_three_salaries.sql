# Write your MySQL query statement below


select 
    t1.Department as Department, 
    t1.Employee as Employee, 
    t1.Salary as Salary
from 
    (
        select 
            rownum, 
            tmp.Name as Employee, 
            tmp.Salary, tmp.DepartmentId, 
            Department.Name as Department 
        from 
            (
                select 
                    CAST((@row := @row + 1) AS UNSIGNED) as rownum, 
                    Name, 
                    Salary, 
                    DepartmentId
                from 
                    (select (@row := 0)) as tmp1,
                    (
                        select 
                            Name, 
                            Salary, 
                            DepartmentId
                        from 
                            Employee
                        order by 
                            DepartmentId asc, 
                            Salary desc
                    ) as tmp2
            ) as tmp left join Department
        on tmp.DepartmentId = Department.Id
    ) as t1,
    (
        select 
            CAST((@row := @row + 1) AS UNSIGNED) as rownum, 
            Name, 
            Salary, 
            DepartmentId
        from 
            (select (@row := 0)) as tmp1,
            (
                select Name, Salary, DepartmentId
                from 
                    Employee
                order by DepartmentId asc, Salary desc
            ) as tmp2
    ) as t2
where
    t1.rownum < t2.rownum and 
    
    (
        t1.rownum <= 3
    ) 
    -- or 
    -- (
    --     t1.rownum=t2.rownum+3
    --     and t1.DepartmentId <> t2.DepartmentId
    -- )
    