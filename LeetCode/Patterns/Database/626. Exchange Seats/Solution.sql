# Write your MySQL query statement below

-- select id-1 , student from Seat
-- where (id-1) in  
-- (select id from Seat
-- where id % 2 <> 0)

-- select id+1 , student from Seat
-- where (id+1) in  
-- (select id from Seat
-- where id % 2 = 0)

with cte as (select count(*) as count from Seat)

select case
        when id = (select count from cte)  and (select count from cte) %2 <> 0  then id
        when id % 2 <> 0 then id + 1
        else id-1
        end as id, student
from Seat
order by id