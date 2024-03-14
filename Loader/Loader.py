import psycopg
import json

pwd = ""

# assumes the data location
with open('../open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/competitions.json', 'r') as file:
    competitions = json.load(file)

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password={pwd}") as conn:
    with conn.cursor() as cur:

        # COMPETITIONS
        cur.execute(open("competitions.sql", "r").read())
        for row in competitions:
            cur.execute("""
                INSERT INTO competitions (competition_id, 
                                          season_id, 
                                          country_name, 
                                          competition_name,
                                          competition_gender,
                                          competition_youth,
                                          competition_international,
                                          season_name,
                                          match_updated,
                                          match_updated_360,
                                          match_available_360,
                                          match_available)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (row['competition_id'],
                  row['season_id'],
                  row['country_name'],
                  row['competition_name'],
                  row['competition_gender'],
                  row['competition_youth'],
                  row['competition_international'],
                  row['season_name'],
                  row['match_updated'],
                  row['match_updated_360'],
                  row['match_available_360'],
                  row['match_available']))

        cur.execute("SELECT * FROM competitions")
        cur.fetchone()

        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
