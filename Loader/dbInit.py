import psycopg

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
        # DROP EVERY TABLE
        cur.execute("""
            DROP TABLE IF EXISTS competition_stages,
                                 competitions,
                                 countries,
                                 managers,
                                 match_competition,
                                 matches,
                                 seasons,
                                 stadiums,
                                 teams;
            """)

        cur.execute(open("Loader/sqlInit/competitions.sql", "r").read())
        conn.commit()
        cur.execute(open("Loader/sqlInit/matches.sql", "r").read())
        conn.commit()
        # cur.execute(open("Loader/sqlInit/teams.sql", "r").read())
        # cur.execute(open("Loader/sqlInit/players.sql", "r").read())
        # cur.execute(open("Loader/sqlInit/events.sql", "r").read())
        # cur.execute(open("Loader/sqlInit/lineups.sql", "r").read())
        # cur.execute(open("Loader/sqlInit/lineupPlayers.sql", "r").read())

        conn.commit()
        # conn.close()

print("\tRelations: competitions, matches, events, lineups, teams, lineupPlayers, and players have been initialized.")
