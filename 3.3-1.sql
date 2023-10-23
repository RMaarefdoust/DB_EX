DROP VIEW IF EXISTS autorid;
CREATE VIEW autorid AS 
select Author_id
from Author
where FNAME like 'Wei' AND LNAME like 'Wu';

