import psycopg

with psycopg.connect("dbname=comp3005finalproject user=postgres password=Turnbull01!") as conn:
    with conn.cursor() as cur:
        # Initiate tables 
        #f = open("test.txt","r")
        cur.execute(open("competitions.sql", "r").read())
        cur.execute(open("linups.sql", "r").read())
        cur.execute(open("lineupPlayers.sql", "r").read())
