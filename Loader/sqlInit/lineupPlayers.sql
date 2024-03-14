-- TODO

-- COMPETITIONS
create table lineupPlayers
(
    match_id    integer,
    team_id     integer,
    player_id   integer,

    PRIMARY KEY (match_id, team_id, player_id),
    FOREIGN KEY (match_id) REFERENCES matches (match_id),
    FOREIGN KEY (team_id) REFERENCES teams (team_id),
    FOREIGN KEY (player_id) REFERENCES players (player_id)
);
