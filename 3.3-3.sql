select Count(distinct(LNAME))as coauthored
from Author
where Author_id in (
select  s.Author_ID
from writer s
where s.Paper_ID in (select Paper_ID from paperid));


	