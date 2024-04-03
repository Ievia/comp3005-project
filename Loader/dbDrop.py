#FOR TESTING PURPOSES

#USE PROGRAM TO DROP ALL TABLES TO TEST LOADING THEM

import psycopg

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
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
        conn.commit()
