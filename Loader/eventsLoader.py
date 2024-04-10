import psycopg
import os
import json

with psycopg.connect(f"dbname=comp3005finalproject user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
        eventsDir = 'open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/events'

        # get all match_id's
        cur.execute("SELECT match_id FROM matches")
        match_ids = [match_id[0] for match_id in cur.fetchall()]

        for f in os.listdir(eventsDir):
            match_id = int(f.split('.')[0])
            if match_id in match_ids:
                with open(eventsDir + '/' + f, 'r') as file:
                    events = json.load(file)

                for row in events:
                    # event type
                    cur.execute("""
                        INSERT INTO event_type (id, name)
                        VALUES (%s, %s)
                        ON CONFLICT (id) DO NOTHING;
                    """, (row['type']['id'],
                          row['type']['name']))
                    conn.commit()

                    # play pattern
                    cur.execute("""
                        INSERT INTO play_pattern (id, name)
                        VALUES (%s, %s)
                        ON CONFLICT (ID) DO NOTHING 
                    """, (row['play_pattern']['id'],
                          row['play_pattern']['name']))
                    conn.commit()

                    # event
                    cur.execute("""
                        SELECT season_id
                        FROM matches
                        WHERE match_id = %s
                    """, (match_id,))
                    season_id = cur.fetchone()[0]
                    cur.execute("""
                        INSERT INTO event (id, 
                                           index, 
                                           period, 
                                           timestamp, 
                                           minute, 
                                           second, 
                                           event_type_id, 
                                           possession, 
                                           possession_team_id, 
                                           play_pattern_id, 
                                           team_id, 
                                           duration,
                                           season_id) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (id) DO NOTHING;
                    """, (row['id'],
                          row['index'],
                          row['period'],
                          row['timestamp'],
                          row['minute'],
                          row['second'],
                          row['type']['id'],
                          row['possession'],
                          row['possession_team']['id'],
                          row['play_pattern']['id'],
                          row['team']['id'],
                          row.get('duration', None),
                          season_id))
                    conn.commit()

                    # tactics
                    # FIXME this is really weird
                    if row.get('tactics', None) is not None:
                        for lineup in row['tactics']['lineup']:
                            cur.execute("""
                                INSERT INTO tactics (event_id, 
                                                     formation, 
                                                     player_id, 
                                                     position_id, 
                                                     jersey_number)
                                VALUES (%s, %s, %s, %s, %s)
                                ON CONFLICT (event_id, formation) DO NOTHING;
                            """, (row['id'],
                                  row['tactics']['formation'],
                                  lineup['player']['id'],
                                  lineup['position']['id'],
                                  lineup['jersey_number']))
                        conn.commit()

                    # shot
                    if row['type']['id'] == 16:
                        cur.execute("""
                            INSERT INTO shot (event_id, player_id, statsbomb_xg)
                            VALUES (%s, %s, %s)
                            ON CONFLICT (event_id, player_id) DO NOTHING;
                        """, (row['id'],
                              row['player']['id'],
                              row['shot']['statsbomb_xg']))
                    conn.commit()
