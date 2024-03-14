create table matches
(
    match_id            integer,
    competition_id      integer,
    competition_name    varchar,
    PRIMARY KEY(match_id),
    FOREIGN KEY (competition_id) REFERENCES competitions (competition_id)
);