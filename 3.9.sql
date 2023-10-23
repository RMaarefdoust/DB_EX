select Author_id, FNAME, LNAME
from (
    select Author_id, FNAME, LNAME, COUNT(*) AS registration_count
    from author
    group by FNAME, LNAME
) as subquery
where registration_count = 1;
