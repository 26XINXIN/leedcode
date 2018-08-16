select Distinct p1.Email
from 
    Person as p1,
    Person as p2
where
    p1.Id <> p2.Id
    and p1.Email=p2.Email;