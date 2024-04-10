create table competitions
(
    competition_id            integer,
    season_id                 integer,
    country_name              varchar,
    competition_name          varchar,
    competition_gender        varchar,
    competition_youth         bool,
    competition_international bool,
    season_name               varchar,
    PRIMARY KEY (competition_id, season_id)
);
