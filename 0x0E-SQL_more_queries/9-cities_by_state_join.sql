-- lists all cities contained in the database hbtn_0d_usa.
SELECT c.id As id,c.name AS name,s.name AS name
FROM cities c, states s
WHERE s.id = c.state_id
ORDER BY c.id;