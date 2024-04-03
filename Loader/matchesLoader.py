import psycopg
import os
import json

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
        match_directory = 'open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches'

        for root, dirs, files in os.walk(match_directory):
            if (dirs == 11 and files in [90, 42, 4]) or \
                    (dirs == 2 and files == 44):
                with open(match_directory + f'/{dirs}/{files}', 'r') as file:
                    matches = json.load(file)

                for row in matches:
                    cur.execute("""
                        INSERT INTO matches (match_id,
                                             match_date,
                                             kick_off,
                                             competition_id,
                                             season_id,
                                             home_team_id,
                                             away_team_id,
                                             home_score,
                                             away_score,
                                             match_status,
                                             match_status_360,
                                             last_updated,
                                             last_updated_360,
                                             data_version,
                                             shot_fidelity_version,
                                             xy_fidelity_version,
                                             match_week,
                                             competition_stage_id,
                                             stadium_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (row['match_id'],
                          row['match_date'],
                          row['competition']['competition_id'],
                          row['season']['season_id'],
                          row['home_team']['home_team_id'],
                          row['away_team']['away_team_id'],
                          ))

        cur.execute("SELECT * FROM matches")
        cur.fetchone()

        for record in cur:
            print(record)

# Make the changes to the database persistent
conn.commit()
conn.close()
