select p.Title
from paper as p , cite as c
where c.Paper_id=p.Paper_id and c.Cite= '[]'