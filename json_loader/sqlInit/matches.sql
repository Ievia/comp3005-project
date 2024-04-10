CREATE TABLE match_competition
(
    competition_id   integer PRIMARY KEY,
    country_name     varchar,
    competition_name varchar
);

CREATE TABLE seasons
(
    season_id   integer PRIMARY KEY,
    season_name varchar
);

CREATE TABLE countries
(
    country_id   integer PRIMARY KEY,
    country_name varchar
);

CREATE TABLE competition_stages
(
    stage_id   integer PRIMARY KEY,
    stage_name varchar
);

CREATE TABLE referees
(
    referee_id   integer PRIMARY KEY,
    referee_name varchar,
    country_id   integer,
    FOREIGN KEY (country_id) REFERENCES countries (country_id)
);

CREATE TABLE managers
(
    manager_id       integer PRIMARY KEY,
    manager_name     varchar,
    manager_nickname varchar,
    manager_dob      date,
    country_id       integer,
    FOREIGN KEY (country_id) REFERENCES countries (country_id)
);

CREATE TABLE teams
(
    team_id     integer PRIMARY KEY,
    team_name   varchar,
    team_gender varchar,
    team_group  varchar,
    country_id  integer,
    manager_id  integer,
    FOREIGN KEY (country_id) REFERENCES countries (country_id),
    FOREIGN KEY (manager_id) REFERENCES managers (manager_id)
);

CREATE TABLE stadiums
(
    stadium_id   integer PRIMARY KEY,
    stadium_name varchar,
    country_id   integer,
    FOREIGN KEY (country_id) REFERENCES countries (country_id)
);


CREATE TABLE matches
(
    match_id              integer PRIMARY KEY,
    match_date            date,
    kick_off              time,
    competition_id        integer,
    season_id             integer,
    home_team_id          integer,
    away_team_id          integer,
    home_score            integer,
    away_score            integer,
    match_week            integer,
    competition_stage_id  integer,
    stadium_id            integer,
    referee_id            integer,
    FOREIGN KEY (competition_id, season_id)  REFERENCES competitions (competition_id, season_id),
    FOREIGN KEY (competition_id) REFERENCES match_competition (competition_id),
    FOREIGN KEY (season_id) REFERENCES seasons (season_id),
    FOREIGN KEY (home_team_id) REFERENCES teams (team_id),
    FOREIGN KEY (away_team_id) REFERENCES teams (team_id),
    FOREIGN KEY (competition_stage_id) REFERENCES competition_stages (stage_id),
    FOREIGN KEY (stadium_id) REFERENCES stadiums (stadium_id),
    FOREIGN KEY (referee_id) REFERENCES referees (referee_id)
);
