CREATE TABLE event_type
(
    id   integer PRIMARY KEY,
    name varchar
);

CREATE TABLE play_pattern
(
    id   integer PRIMARY KEY,
    name varchar
);

CREATE TABLE event
(
    id                 varchar PRIMARY KEY,
    index              integer,
    period             integer,
    timestamp          varchar,
    minute             integer,
    second             integer,
    event_type_id      integer,
    possession         integer,
    possession_team_id integer,
    play_pattern_id    integer,
    team_id            integer,
    duration           decimal,
    FOREIGN KEY (possession_team_id) REFERENCES comp3005finalproject.public.teams (team_id),
    FOREIGN KEY (play_pattern_id) REFERENCES play_pattern (id),
    FOREIGN KEY (team_id) REFERENCES comp3005finalproject.public.teams (team_id)
);

CREATE TABLE tactics
(
    event_id      varchar,
    formation     integer,
    player_id     integer,
    position_id   integer,
    jersey_number integer,
    PRIMARY KEY (event_id, formation),
    FOREIGN KEY (event_id) REFERENCES event (id),
    FOREIGN KEY (player_id) REFERENCES comp3005finalproject.public.player (player_id),
    FOREIGN KEY (player_id, position_id) REFERENCES comp3005finalproject.public.position (player_id, position_id)
);
