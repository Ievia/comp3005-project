import psycopg
import os
import json

with psycopg.connect(f"dbname=project_database host=localhost user=postgres password=1234") as conn:
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
                        INSERT INTO event_types (id, name)
                        VALUES (%s, %s)
                        ON CONFLICT (id) DO NOTHING;
                    """, (row['type']['id'],
                          row['type']['name']))
                    conn.commit()

                    # play pattern
                    cur.execute("""
                        INSERT INTO play_patterns (id, name)
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
                        INSERT INTO events (id, 
                                            season_id,
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
                                            duration) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (id) DO NOTHING;
                    """, (row['id'],
                          season_id,
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
                          row.get('duration', None)))
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
                            INSERT INTO shots (event_id, 
                                               player_id,
                                               team_id, 
                                               statsbomb_xg,
                                               first_time)
                            VALUES (%s, %s, %s, %s, %s);
                        """, (row['id'],
                              row['player']['id'],
                              row['team']['id'],
                              row['shot']['statsbomb_xg'],
                              row['shot'].get('first_time', False)))
                    conn.commit()

                    # pass
                    if row['type']['id'] == 30:
                        recipient = row['pass'].get('recipient', None)
                        if recipient is not None:
                            recipient_id = recipient.get('id', None)
                        else:
                            recipient_id = None
                        cur.execute("""
                            INSERT INTO passes (event_id, 
                                                team_id, 
                                                player_id,
                                                recipient_id,
                                                through_ball)
                            VALUES (%s, %s, %s, %s, %s);
                        """, (row['id'],
                              row['team']['id'],
                              row['player']['id'],
                              recipient_id,
                              row['pass'].get('through_ball', False)))
                    conn.commit()

                    # dribble
                    if row['type']['id'] == 14:
                        cur.execute("""
                            INSERT INTO dribbles (event_id, player_id, outcome_id, outcome_name)
                            VALUES (%s, %s, %s, %s)
                        """, (row['id'],
                              row['player']['id'],
                              row['dribble']['outcome']['id'],
                              row['dribble']['outcome']['name']))
                    conn.commit()

                    # dribbled past
                    if row['type']['id'] == 39:
                        cur.execute("""
                            INSERT INTO dribbled_past(event_id, player_id)
                            VALUES (%s, %s)
                        """, (row['id'],
                              row['player']['id']))
