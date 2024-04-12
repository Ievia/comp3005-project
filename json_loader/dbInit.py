import psycopg

with psycopg.connect(f"dbname=project_database host=localhost user=postgres password=1234") as conn:
    with conn.cursor() as cur:
        # DROP EVERY TABLE
        cur.execute("""
            DROP TABLE IF EXISTS cards,
                                 competition_stages,
                                 competitions,
                                 countries,
                                 dribbles,
                                 dribbled_past,
                                 event_type,
                                 events,
                                 lineups,
                                 managers,
                                 match_competitions,
                                 matches,
                                 passes,
                                 play_patterns,
                                 players,
                                 positions,
                                 referees,
                                 seasons,
                                 shots,
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
