select Paper.Title
from Paper
inner join writer on Paper.Paper_id = writer.Paper_id
inner join Author on writer.Author_id = Author.Author_id
where Author.FNAME like 'Minoru' and Author.LNAME like 'Eto';
