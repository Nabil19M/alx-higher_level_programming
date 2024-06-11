--  lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT  C.id, C.name
FROM states S, cities C
WHERE S.id = C.state_id AND S.name = "California"
ORDER BY C.id ASC;