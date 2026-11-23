# Write your MySQL query statement below
with cte as
(select * from MovieRating where month(created_at) = 2 and year(created_at) = 2020)

(select u.name as results from Users u
join MovieRating mr
on u.user_id = mr.user_id
group by mr.user_id
order by count(mr.movie_id) desc, ord(u.name)
limit 1)

union all

(select  m.title as results from Movies m
join cte c
on m.movie_id = c.movie_id
group by c.movie_id
order by avg(rating) desc, ord(m.title)
limit 1)

