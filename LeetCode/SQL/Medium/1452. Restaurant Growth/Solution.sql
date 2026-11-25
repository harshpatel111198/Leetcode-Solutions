-- Write your PostgreSQL query statement below



with day_sale as (select visited_on, sum(amount) as amount
from Customer
group by visited_on
order by visited_on)

select visited_on,
round(sum(amount) over(order by visited_on rows between 6 preceding and current row), 2) as amount,
round(avg(amount) over(order by visited_on rows between 6 preceding and current row), 2) as average_amount
from day_sale offset 6;