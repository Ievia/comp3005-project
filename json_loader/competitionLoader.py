import psycopg
import json

# assumes the data locations
with open('open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/competitions.json', 'r') as file:
    competitions = json.load(file)

with psycopg.connect(f"dbname=project_database host=localhost user=postgres password=1234") as conn:
    with conn.cursor() as cur:

        # COMPETITIONS
        for row in competitions:
            # filters only the seasons we need
            if (row['competition_id'] == 11 and row['season_id'] in [90, 42, 4]) or \
               (row['competition_id'] == 2 and row['season_id'] == 44):
                cur.execute("""
                    INSERT INTO competitions (competition_id, 
                                              season_id, 
                                              country_name, 
                                              competition_name,
                                              competition_gender,
                                              competition_youth,
                                              competition_international,
                                              season_name) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """, (row['competition_id'],
                          row['season_id'],
                          row['country_name'],
                          row['competition_name'],
                          row['competition_gender'],
                          row['competition_youth'],
                          row['competition_international'],
                          row['season_name']))

        # Make the changes to the database persistent
        conn.commit()
        conn.close()
