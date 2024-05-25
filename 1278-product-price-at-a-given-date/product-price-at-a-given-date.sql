# Write your MySQL query statement below
-- DECLARE @min_date DATE = '2019-08-16';






-- SELECT mainP.product_id as product_id, mainP.new_price as price
-- FROM Products mainP
-- WHERE (mainP.product_id, mainP.change_date )
--         in (
--             SELECT subp.product_id , max(subp.change_date) 
--             FROM Products subp 
--             where subp.change_date <= '2019-08-16'
--             GROUP BY product_id
--             ) 
        
-- GROUP BY product_id

-- UNION 

-- SELECT unionP.product_id as product_id, 10 as price
-- FROM Products unionP
-- WHERE unionP.product_id not in 
--     (
--         select distinct subQ.product_id
--         from Products subQ
--         where (subQ.change_date ) <= '2019-08-16'
--         -- group by subQ.product_id
--         -- having min(subQ.change_date ) > '2019-08-16'
--     )      
-- GROUP BY unionP.product_id


WITH RelevantProducts AS (
    SELECT 
        subp.product_id,
        MAX(subp.change_date) AS max_change_date
    FROM Products subp 
    WHERE subp.change_date <= '2019-08-16'
    GROUP BY subp.product_id
)

SELECT 
    mainP.product_id AS product_id, 
    mainP.new_price AS price
FROM Products mainP
JOIN RelevantProducts rp ON mainP.product_id = rp.product_id AND mainP.change_date = rp.max_change_date

UNION

SELECT 
    unionP.product_id AS product_id, 
    10 AS price
FROM Products unionP
WHERE unionP.product_id NOT IN (
    SELECT distinct product_id FROM RelevantProducts
)
