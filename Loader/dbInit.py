import psycopg

pwd = "Turnbull01!"

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password={pwd}") as conn:
    with conn.cursor() as cur:
        #DROP EVERY TABLE
        cur.execute("DROP TABLE IF EXISTS competitions, matches, events, lineups, teams, lineupPlayers, players;")

        cur.execute(open("loader/sqlInit/competitions.sql", "r").read())
        cur.execute(open("loader/sqlInit/matches.sql", "r").read())
        cur.execute(open("loader/sqlInit/teams.sql", "r").read())
        cur.execute(open("loader/sqlInit/players.sql", "r").read())
        cur.execute(open("loader/sqlInit/events.sql", "r").read())
        cur.execute(open("loader/sqlInit/lineups.sql", "r").read())
        cur.execute(open("loader/sqlInit/lineupPlayers.sql", "r").read())

        conn.commit()