CREATE TABLE event_types
(
    id   integer PRIMARY KEY,
    name varchar
);

CREATE TABLE play_patterns
(
    id   integer PRIMARY KEY,
    name varchar
);

CREATE TABLE events
(
    id                 varchar PRIMARY KEY,
    season_id          integer,
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
    FOREIGN KEY (season_id) REFERENCES project_database.public.seasons (season_id),
    FOREIGN KEY (possession_team_id) REFERENCES project_database.public.teams (team_id),
    FOREIGN KEY (play_pattern_id) REFERENCES play_patterns (id),
    FOREIGN KEY (team_id) REFERENCES project_database.public.teams (team_id)
);
CREATE INDEX ON events (season_id);

CREATE TABLE tactics
(
    event_id      varchar,
    formation     integer,
    player_id     integer,
    position_id   integer,
    jersey_number integer,
    PRIMARY KEY (event_id, formation),
    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (player_id) REFERENCES project_database.public.players (player_id),
    FOREIGN KEY (player_id, position_id) REFERENCES project_database.public.positions (player_id, position_id)
);

CREATE TABLE shots
(
    event_id     varchar,
    player_id    integer,
    team_id      integer,
    statsbomb_xg decimal,
    first_time   boolean,
    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (player_id) REFERENCES project_database.public.players (player_id),
    FOREIGN KEY (team_id) REFERENCES project_database.public.teams (team_id)
);
CREATE UNIQUE INDEX ON shots (event_id);
CREATE INDEX ON shots (player_id);
CREATE INDEX ON shots (team_id);
CREATE INDEX ON shots (statsbomb_xg);
CREATE INDEX ON shots (first_time);
-- CREATE UNIQUE INDEX ON shot (event_id, player_id, statsbomb_xg);

CREATE TABLE passes
(
    event_id     varchar,
    team_id      integer,
    player_id    integer,
    recipient_id integer,
    through_ball boolean,
    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (team_id) REFERENCES project_database.public.teams (team_id),
    FOREIGN KEY (recipient_id) REFERENCES project_database.public.players (player_id)
);
CREATE UNIQUE INDEX ON passes (event_id);
CREATE INDEX ON passes (player_id);
CREATE INDEX ON passes (team_id);
CREATE INDEX ON passes (recipient_id);
CREATE INDEX ON passes (through_ball);

CREATE TABLE dribbles
(
    event_id     varchar,
    player_id    integer,
    outcome_id   integer,
    outcome_name varchar,
    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (player_id) REFERENCES project_database.public.players (player_id)
);
CREATE UNIQUE INDEX ON dribbles (event_id);
CREATE INDEX ON dribbles (player_id);
CREATE INDEX ON dribbles (outcome_id);

CREATE TABLE dribbled_past
(
    event_id  varchar,
    player_id integer,
    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (player_id) REFERENCES project_database.public.players (player_id)
);
CREATE UNIQUE INDEX ON dribbled_past (event_id);
CREATE INDEX ON dribbled_past (player_id);
