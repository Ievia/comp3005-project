CREATE TABLE player
(
    player_id       integer PRIMARY KEY,
    player_name     varchar,
    player_nickname varchar,
    jersey_number   integer,
    country_id      integer,
    FOREIGN KEY (country_id) REFERENCES project_database.public.countries (country_id)
);
CREATE UNIQUE INDEX ON player (player_name);
-- CREATE UNIQUE INDEX ON player (player_id, player_name);

-- NOTE: from_time and to_time are varchars, NOT TIME
CREATE TABLE position
(
    player_id     integer,
    position_id   integer,
    position_name varchar,
    from_time     varchar,
    to_time       varchar,
    from_period   integer,
    to_period     integer,
    start_reason  varchar,
    end_reason    varchar,
    PRIMARY KEY (player_id, position_id),
    FOREIGN KEY (player_id) REFERENCES player (player_id)
);

CREATE TABLE card
(
    match_id  integer,
    player_id integer,
    time      varchar,
    card_type varchar,
    reason    varchar,
    period    integer,
    PRIMARY KEY (match_id, player_id, time),
    FOREIGN KEY  (match_id) REFERENCES project_database.public.matches (match_id),
    FOREIGN KEY (player_id) REFERENCES player (player_id)
);


CREATE TABLE lineup
(
    match_id     integer,
    team_id      integer,
    player_id    integer,
    PRIMARY KEY (match_id, team_id, player_id),
    FOREIGN KEY (match_id) REFERENCES project_database.public.matches (match_id),
    FOREIGN KEY (team_id) REFERENCES project_database.public.teams (team_id),
    FOREIGN KEY (player_id) REFERENCES player (player_id)
);
