-- Write your PostgreSQL query statement below



with day_sale as (
    select visited_on, sum(amount) as amount
    from Customer
    group by visited_on),

windowed as (
    select visited_on,
        sum(amount) over w as amount,
        round((sum(amount) over w)/7, 2) as average_amount,
        min(visited_on) over() as first_day
    from day_sale
    window w as (
        order by visited_on
        range between interval '6 days' preceding and current row
    )
)

SELECT visited_on, amount, average_amount
FROM windowed
WHERE visited_on >= first_day + 6 
ORDER BY visited_on;
