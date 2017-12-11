drop table puppy_ex;
drop table puppy;
drop table shelter;

UPDATE shelter S SET current_occupancy = SM.occupancy from (SELECT shelter_id, count(*) AS occupancy FROM puppy GROUP BY shelter_id) AS SM WHERE S.id = SM.shelter_id;