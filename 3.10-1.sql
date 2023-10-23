DROP VIEW IF EXISTS spid;
CREATE VIEW spid AS
SELECT w.Paper_id
FROM writer w
WHERE w.Author_id in (SELECT Author_id FROM Author WHERE FNAME like 'Indranath' AND LNAME like 'Sengupta')