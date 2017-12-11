-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


create database tournament;

create table players (
	name text,
	id serial,
	PRIMARY KEY(id)
);

create table matches (
	winner integer REFERENCES players(id),
	loser integer REFERENCES players(id),
	id serial,
	PRIMARY KEY(id)
);

create view STANDINGS as (
select R.id, R.name, sum(R.WINS) as WINS, sum(R.TOTAL) as TOTAL from (
select P.id, P.name, count(M.winner) as WINS, count(M.winner) as TOTAL
from players P left join matches M ON P.id = M.winner group by P.id
UNION
select P.id, P.name, 0 as WINS, count(M.loser) as TOTAL
from players P left join matches M ON P.id = M.loser group by P.id
) as R group by R.id, R.name);