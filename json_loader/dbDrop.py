#FOR TESTING PURPOSES

#USE PROGRAM TO DROP ALL TABLES TO TEST LOADING THEM

import psycopg

with psycopg.connect(f"dbname=project_database user=postgres password=1234") as conn:
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
                                 shot,
                                 stadiums,
                                 tactics,
                                 teams;
            """)
        conn.commit()
