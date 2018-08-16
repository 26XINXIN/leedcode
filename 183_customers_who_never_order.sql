select Customers.Name as Customers 
from (
    Customers left join (
        select Id as OrderId, CustomerId
        from Orders
    ) as newOrders
    on Customers.id = newOrders.CustomerId
)
where newOrders.OrderId is null;