-- TODO

-- COMPETITIONS
create table lineups
(
    match_id                  integer,
    team_id_away              integer,               
    team_id_home              integer,

    PRIMARY KEY (match_id)
    -- FOREIGN KEY (match_id) REFERENCES matches (match_id)

);
