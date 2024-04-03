#FOR TESTING PURPOSES

#USE PROGRAM TO DROP ALL TABLES TO TEST LOADING THEM

import psycopg

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            DROP TABLE IF EXISTS card,
                                 competition_stages,
                                 competitions,
                                 countries,
                                 event,
                                 event_type,
                                 lineup,
                                 managers,
                                 match_competition,
                                 matches,
                                 play_pattern,
                                 player,
                                 position,
                                 referees,
                                 seasons,
                                 stadiums,
                                 tactics,
                                 teams;
            """)
        conn.commit()
