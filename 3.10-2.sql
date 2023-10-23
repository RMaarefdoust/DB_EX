select count(p.Paper_id) as NumberOfPaper
from spid as p
where p.Paper_id in (
    select w.Paper_id
    from writer as w
    group by  w.Paper_id
    having count(distinct w.Author_id) = 1 OR count(distinct w.Author_id) = 2
)
;
