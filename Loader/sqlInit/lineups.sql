-- TODO

-- COMPETITIONS
create table lineups
(
    match_id                  integer,
    team_id_away              varchar,               
    team_id_home              varchar,

    PRIMARY KEY (match_id),
    FOREIGN KEY (match_id) REFERENCES matches (match_id)

);
