import psycopg
import os
import json

pwd = "Turnbull01!"

# assumes the data location

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password={pwd}") as conn:
    with conn.cursor() as cur:
        competitionDirectory = os.listdir("D:/COMP3005Final/open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches")

        for competition_id in competitionDirectory:
            seasonDirectory = os.listdir(f"D:/COMP3005Final/open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches/{competition_id}")
            for season_id_Filename in seasonDirectory:
                file = open(f'D:/COMP3005Final/open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches/{competition_id}/{season_id_Filename}',errors='replace')
                match = json.load(file)
                
                for row in match:
                    #print(row['competition_id'])
                    cur.execute("""
                    INSERT INTO matches (match_id, 
                                            competition_id, 
                                            competition_name)
                    VALUES(%s,%s,%s);""",
                    (row['match_id'],
                     row['competition']['competition_id'],
                     row['competition']['competition_name']))                

        cur.execute("SELECT * FROM matches")
        cur.fetchone()

        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
