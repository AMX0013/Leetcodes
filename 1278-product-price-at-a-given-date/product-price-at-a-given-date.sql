# Write your MySQL query statement below
-- DECLARE @min_date DATE = '2019-08-16';

SELECT mainP.product_id as product_id, mainP.new_price as price
FROM Products mainP
WHERE mainP.change_date 
        BETWEEN (
            SELECT max(subp.change_date) 
            FROM Products subp 
            where mainP.product_id = subp.product_id 
                and subp.change_date <= '2019-08-16'
            GROUP BY product_id) 
        AND  '2019-08-16'
GROUP BY product_id

UNION 

SELECT unionP.product_id as product_id, 10 as price
FROM Products unionP
WHERE unionP.product_id in 
    (
        select subQ.product_id
        from Products subQ
        group by subQ.product_id
        having min(subQ.change_date ) > '2019-08-16'
    )      
GROUP BY unionP.product_id