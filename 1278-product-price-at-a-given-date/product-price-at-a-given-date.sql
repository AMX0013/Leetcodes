# Write your MySQL query statement below
-- DECLARE @min_date DATE = '2019-08-16';

SELECT mainP.product_id as product_id, mainP.new_price as price
FROM Products mainP
WHERE (mainP.product_id, mainP.change_date )
        in (
            SELECT subp.product_id , max(subp.change_date) 
            FROM Products subp 
            where subp.change_date <= '2019-08-16'
            GROUP BY product_id
            ) 
        
GROUP BY product_id

UNION 

SELECT unionP.product_id as product_id, 10 as price
FROM Products unionP
WHERE unionP.product_id not in 
    (
        select distinct subQ.product_id
        from Products subQ
        where (subQ.change_date ) <= '2019-08-16'
        -- group by subQ.product_id
        -- having min(subQ.change_date ) > '2019-08-16'
    )      
GROUP BY unionP.product_id