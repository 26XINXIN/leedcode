delete from Person
where id in (
    select id from (
        select t1.id 
        from 
            Person t1,
            Person t2
        where 
            t1.id > t2.id 
            and t1.Email = t2.Email
    ) as a
);
