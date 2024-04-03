import psycopg
import os
import json

pwd = "Turnbull01!"

# assumes the data location

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password={pwd}") as conn:
    with conn.cursor() as cur:
        matchesDirectory = os.listdir("D:/COMP3005Final/open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/lineups")

        for lineup_Filename in matchesDirectory:
            file = open(f'D:/COMP3005Final/open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/lineups/{lineup_Filename}',errors='replace')
            lineup = json.load(file)

            match_id = lineup_Filename[:len(lineup_Filename)-5]

            cur.execute("""
            INSERT INTO lineups (match_id, 
                                    team_id_home, 
                                    team_id_away)
            VALUES(%s,%s,%s);""",
            (match_id,
                lineup[0]['team_id'],
                lineup[1]['team_id']))                
        cur.execute("SELECT * FROM lineups")
        cur.fetchone()

        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
