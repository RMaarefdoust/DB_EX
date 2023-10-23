select count(c.Paper_id)
from Cite as c,pidCite as p
where c.Cite like '%' || p.Paper_id || '%'
