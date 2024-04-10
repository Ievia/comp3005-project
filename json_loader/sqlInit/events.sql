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
    season_id          integer,
    FOREIGN KEY (possession_team_id) REFERENCES project_database.public.teams (team_id),
    FOREIGN KEY (play_pattern_id) REFERENCES play_pattern (id),
    FOREIGN KEY (team_id) REFERENCES project_database.public.teams (team_id),
    FOREIGN KEY (season_id) REFERENCES project_database.public.seasons (season_id)
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
    FOREIGN KEY (player_id) REFERENCES project_database.public.player (player_id),
    FOREIGN KEY (player_id, position_id) REFERENCES project_database.public.position (player_id, position_id)
);

CREATE TABLE shot
(
    event_id     varchar,
    player_id    integer,
    team_id      integer,
    statsbomb_xg decimal,
    first_time   boolean,
    FOREIGN KEY (event_id) REFERENCES event (id),
    FOREIGN KEY (player_id) REFERENCES project_database.public.player (player_id),
    FOREIGN KEY (team_id) REFERENCES project_database.public.teams (team_id)
);

CREATE TABLE pass
(
    event_id     varchar,
    team_id      integer,
    player_id    integer,
    recipient_id integer,
    through_ball boolean,
    FOREIGN KEY (event_id) REFERENCES event (id),
    FOREIGN KEY (team_id) REFERENCES project_database.public.teams (team_id),
    FOREIGN KEY (recipient_id) REFERENCES project_database.public.player (player_id)
);

CREATE TABLE dribble
(
    event_id  varchar,
    player_id integer,
    outcome   varchar,
    FOREIGN KEY (event_id) REFERENCES event (id),
    FOREIGN KEY (player_id) REFERENCES project_database.public.player (player_id)
);

CREATE TABLE dribbled_past
(
    event_id  varchar,
    player_id integer,
    FOREIGN KEY (event_id) REFERENCES event (id),
    FOREIGN KEY (player_id) REFERENCES project_database.public.player (player_id)
)
