DROP VIEW IF EXISTS paperid;
CREATE VIEW paperid AS 
select distinct w.Paper_id
from Writer w
inner join autorid a on w.Author_id = a.Author_id;
