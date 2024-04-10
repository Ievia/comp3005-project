import psycopg

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
        # DROP EVERY TABLE
        cur.execute("""
            DROP TABLE IF EXISTS card,
                                 competition_stages,
                                 competitions,
                                 countries,
                                 event,
                                 event_type,
                                 lineup,
                                 managers,
                                 match_competition,
                                 matches,
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

        cur.execute(open("Loader/sqlInit/competitions.sql", "r").read())
        conn.commit()
        cur.execute(open("Loader/sqlInit/matches.sql", "r").read())
        conn.commit()
        cur.execute(open("Loader/sqlInit/lineups.sql", "r").read())
        conn.commit()
        cur.execute(open("Loader/sqlInit/events.sql", "r").read())
        conn.commit()

        # conn.close()
