create table events
(
    event_id        integer,
    match_id        integer,
    PRIMARY KEY (event_id),
    FOREIGN KEY (match_id) REFERENCES matches (match_id)

);