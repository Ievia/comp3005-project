#FOR TESTING PURPOSES

#USE PROGRAM TO DROP ALL TABLES TO TEST LOADING THEM

pwd="Turnbull01!"

import psycopg

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password={pwd}") as conn:
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS competitions, matches, events, lineups, teams, lineupPlayers, players;")
        conn.commit()
