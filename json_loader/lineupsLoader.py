import psycopg
import os
import json

with psycopg.connect(f"dbname=project_database user=postgres password=1234") as conn:
    with conn.cursor() as cur:
        lineupsDir = 'open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/lineups'

        # get all match_id's
        cur.execute("SELECT match_id FROM matches")
        match_ids = [match_id[0] for match_id in cur.fetchall()]

        for f in os.listdir(lineupsDir):
            match_id = int(f.split('.')[0])
            if match_id in match_ids:
                with open(lineupsDir + '/' + f, 'r') as file:
                    lineups = json.load(file)

                for row in lineups:
                    # insert the players
                    for player in row['lineup']:
                        # insert any new countries found here
                        cur.execute("""
                            INSERT INTO countries (country_id, country_name)
                            VALUES (%s, %s)
                            ON CONFLICT (country_id) DO NOTHING;
                        """, (player['country']['id'],
                              player['country']['name']))
                        conn.commit()

                        # actually insert the player
                        cur.execute("""
                            INSERT INTO player (player_id, 
                                                player_name, 
                                                player_nickname, 
                                                jersey_number, 
                                                country_id) 
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (player_id) DO NOTHING;
                        """, (player['player_id'],
                              player['player_name'],
                              player['player_nickname'],
                              player['jersey_number'],
                              player['country']['id']))
                        conn.commit()

                        # insert the positions they played
                        for position in player['positions']:
                            cur.execute("""
                                INSERT INTO position (player_id, 
                                                      position_id, 
                                                      position_name, 
                                                      from_time, 
                                                      to_time, 
                                                      from_period, 
                                                      to_period, 
                                                      start_reason, 
                                                      end_reason) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                ON CONFLICT (player_id, position_id) DO NOTHING;
                            """, (player['player_id'],
                                  position['position_id'],
                                  position.get('position', None),
                                  position.get('from', None),
                                  position.get('to', None),
                                  position.get('from_period', None),
                                  position.get('to_period', None),
                                  position.get('start_reason', None),
                                  position.get('end_reason', None)))
                            conn.commit()

                        for card in player['cards']:
                            cur.execute("""
                                INSERT INTO card (match_id, 
                                                  player_id, 
                                                  time, 
                                                  card_type, 
                                                  reason, 
                                                  period)
                                VALUES (%s, %s, %s, %s, %s, %s)
                                ON CONFLICT (match_id, player_id, time) DO NOTHING;
                            """, (match_id,
                                  player['player_id'],
                                  card['time'],
                                  card['card_type'],
                                  card['reason'],
                                  card['period']))
                        conn.commit()

                        # Lineups
                        cur.execute("""
                                INSERT INTO lineup (match_id, team_id, player_id) 
                                VALUES (%s, %s, %s)
                                ON CONFLICT (match_id, team_id, player_id) DO NOTHING;
                            """, (match_id,
                                  row['team_id'],
                                  player['player_id']))
                        conn.commit()

        conn.commit()
        conn.close()
