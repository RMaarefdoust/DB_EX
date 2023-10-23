DROP VIEW IF EXISTS pidCite;
CREATE VIEW pidCite As
select Paper_id
from writer as w
where w.Author_id in (select Author_id from author where FNAME like 'Lei' and LNAME like 'Yin')

