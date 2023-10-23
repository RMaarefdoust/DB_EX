select paper.Title
from Paper
where Paper_id in (
select Paper_id
from writer
group by Paper_id
having COUNT(Author_id) = 1);
