# Write your MySQL query statement below

select T.id as id,
    case 
        when T.p_id  is null 
        then "Root"
        when T.id  in (select distinct p_id from Tree)
        then "Inner"
        else "Leaf"
    END as type
from Tree T
