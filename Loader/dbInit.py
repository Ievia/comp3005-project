import psycopg

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
        # DROP EVERY TABLE
        cur.execute("""
            DROP TABLE IF EXISTS card,
                                 competition_stages,
                                 competitions,
                                 countries,
                                 lineup,
                                 managers,
                                 match_competition,
                                 matches,
                                 player,
                                 position,
                                 referees,
                                 seasons,
                                 stadiums,
                                 teams;
            """)

        cur.execute(open("Loader/sqlInit/competitions.sql", "r").read())
        conn.commit()
        cur.execute(open("Loader/sqlInit/matches.sql", "r").read())
        conn.commit()
        cur.execute(open("Loader/sqlInit/lineups.sql", "r").read())
        conn.commit()

        conn.commit()
        # conn.close()
