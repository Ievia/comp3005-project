#FOR TESTING PURPOSES

#USE PROGRAM TO DROP ALL TABLES TO TEST LOADING THEM

import psycopg

with psycopg.connect("dbname=comp3005finalproject user=postgres password=Turnbull01!") as conn:
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS competitions, matches, events, lineups, teams, lineupPlayers, players;")
        conn.commit()
