import psycopg

with psycopg.connect(f"dbname=project_database host=localhost user=postgres password=1234") as conn:
    with conn.cursor() as cur:
        # DROP EVERY TABLE
        cur.execute("""
            DROP TABLE IF EXISTS card,
                                 competition_stages,
                                 competitions,
                                 countries,
                                 dribble,
                                 dribbled_past,
                                 event_info,
                                 event_type,
                                 events,
                                 lineup,
                                 managers,
                                 match_competition,
                                 matches,
                                 pass,
                                 play_pattern,
                                 player,
                                 position,
                                 referees,
                                 seasons,
                                 shot,
                                 stadiums,
                                 tactics,
                                 teams;
        """)

        cur.execute(open("json_loader/sqlInit/competitions.sql", "r").read())
        conn.commit()
        cur.execute(open("json_loader/sqlInit/matches.sql", "r").read())
        conn.commit()
        cur.execute(open("json_loader/sqlInit/lineups.sql", "r").read())
        conn.commit()
        cur.execute(open("json_loader/sqlInit/events.sql", "r").read())
        conn.commit()

        # conn.close()
