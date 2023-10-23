select p.Title
from Paper as p
where p.Paper_id<  2101.00200 and p.Paper_id not in (
select a.Paper_id
from Cite as c,paper as a
where a.Paper_id< 2101.00200 and c.cite like '%'||a.Paper_id||'%')