import psycopg
import json

with psycopg.connect(f"dbname=project_database host=localhost user=postgres password=1234") as conn:
    with conn.cursor() as cur:

        # FIXME currently hard coded
        matches_we_need = ['open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches/2/44.json',
                           'open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches/11/4.json',
                           'open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches/11/42.json',
                           'open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches/11/90.json']
        for f in matches_we_need:
            with open(f, 'r') as file:
                matches = json.load(file)
            for row in matches:
                cur.execute("""
                    INSERT INTO match_competitions (competition_id,
                                                    country_name,
                                                    competition_name)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (competition_id) DO NOTHING;
                    """, (row['competition']['competition_id'],
                          row['competition']['country_name'],
                          row['competition']['competition_name']))
                conn.commit()

                cur.execute("""
                    INSERT INTO seasons (season_id, season_name)
                    VALUES (%s, %s)
                    ON CONFLICT (season_id) DO NOTHING;
                """, (row['season']['season_id'],
                      row['season']['season_name']))
                conn.commit()

                # countries can appear 6 different places
                cur.execute("""
                    INSERT INTO countries (country_id, country_name)
                    VALUES (%s, %s)
                    ON CONFLICT (country_id) DO NOTHING;
                """, (row['home_team']['country']['id'],
                      row['home_team']['country']['name']))
                try:
                    for manager in row['home_team']['managers']:
                        cur.execute("""
                            INSERT INTO countries (country_id, country_name)
                            VALUES (%s, %s)
                            ON CONFLICT (country_id) DO NOTHING;
                        """, (manager['country']['id'],
                              manager['country']['name']))
                except KeyError:
                    pass
                cur.execute("""
                    INSERT INTO countries (country_id, country_name)
                    VALUES (%s, %s)
                    ON CONFLICT (country_id) DO NOTHING;
                """, (row['away_team']['country']['id'],
                      row['away_team']['country']['name']))
                try:
                    for managers in row['away_team']['managers']:
                        cur.execute("""
                            INSERT INTO countries (country_id, country_name)
                            VALUES (%s, %s)
                            ON CONFLICT (country_id) DO NOTHING;
                        """, (managers['country']['id'],
                              managers['country']['name']))
                except KeyError:
                    pass
                try:
                    cur.execute("""
                        INSERT INTO countries (country_id, country_name)
                        VALUES (%s, %s)
                        ON CONFLICT (country_id) DO NOTHING;
                    """, (row['referee']['country']['id'],
                          row['referee']['country']['name']))
                except KeyError:
                    pass
                try:
                    cur.execute("""
                        INSERT INTO countries (country_id, country_name)
                        VALUES (%s, %s)
                        ON CONFLICT (country_id) DO NOTHING;
                    """, (row['stadium']['country']['id'],
                          row['stadium']['country']['name']))
                except KeyError:
                    pass
                conn.commit()

                # competition stages
                cur.execute("""
                    INSERT INTO competition_stages (stage_id, stage_name)
                    VALUES (%s, %s)
                    ON CONFLICT (stage_id) DO NOTHING;
                """, (row['competition_stage']['id'],
                      row['competition_stage']['name']))
                conn.commit()

                # referees
                try:
                    cur.execute("""
                        INSERT INTO referees (referee_id, referee_name, country_id) 
                        VALUES (%s, %s, %s)
                        ON CONFLICT (referee_id) DO NOTHING 
                    """, (row['referee']['id'],
                          row['referee']['name'],
                          row['referee']['country']['id']))
                except KeyError:
                    pass

                # managers from home team and away team
                try:
                    for manager in row['home_team']['managers']:
                        cur.execute("""
                            INSERT INTO managers (manager_id,
                                                  manager_name,
                                                  manager_nickname,
                                                  manager_dob,
                                                  country_id)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (manager_id) DO NOTHING;
                        """, (manager['id'],
                              manager['name'],
                              manager['nickname'],
                              manager['dob'],
                              manager['country']['id']))
                except KeyError as e:
                    pass
                try:
                    for manager in row['away_team']['managers']:
                        cur.execute("""
                            INSERT INTO managers (manager_id,
                                                  manager_name,
                                                  manager_nickname,
                                                  manager_dob,
                                                  country_id)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT (manager_id) DO NOTHING;
                        """, (manager['id'],
                              manager['name'],
                              manager['nickname'],
                              manager['dob'],
                              manager['country']['id']))
                except KeyError:
                    pass
                conn.commit()

                # home team and away team
                # some teams don't have managers, so lots of duplicated code here
                try:
                    if row['home_team'].get('managers') is None:
                        cur.execute("""
                            INSERT INTO teams (team_id,
                                               team_name,
                                               team_gender,
                                               team_group,
                                               country_id,
                                               manager_id)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            ON CONFLICT (team_id) DO NOTHING;
                        """, (row['home_team']['home_team_id'],
                              row['home_team']['home_team_name'],
                              row['home_team']['home_team_gender'],
                              row['home_team']['home_team_group'],
                              row['home_team']['country']['id'],
                              None))
                    else:
                        for manager in row['home_team']['managers']:
                            cur.execute("""
                                INSERT INTO teams (team_id,
                                                   team_name,
                                                   team_gender,
                                                   team_group,
                                                   country_id,
                                                   manager_id)
                                VALUES (%s, %s, %s, %s, %s, %s)
                                ON CONFLICT (team_id) DO NOTHING;
                            """, (row['home_team']['home_team_id'],
                                  row['home_team']['home_team_name'],
                                  row['home_team']['home_team_gender'],
                                  row['home_team']['home_team_group'],
                                  row['home_team']['country']['id'],
                                  manager['id']))
                except KeyError:
                    pass
                try:
                    if row['away_team'].get('managers') is None:
                        cur.execute("""
                                INSERT INTO teams (team_id,
                                                   team_name,
                                                   team_gender,
                                                   team_group,
                                                   country_id,
                                                   manager_id)
                                VALUES (%s, %s, %s, %s, %s, %s)
                                ON CONFLICT (team_id) DO NOTHING;
                            """, (row['away_team']['away_team_id'],
                                  row['away_team']['away_team_name'],
                                  row['away_team']['away_team_gender'],
                                  row['away_team']['away_team_group'],
                                  row['away_team']['country']['id'],
                                  manager['id']))
                    else:
                        for manager in row['away_team']['managers']:
                            cur.execute("""
                                INSERT INTO teams (team_id,
                                                   team_name,
                                                   team_gender,
                                                   team_group,
                                                   country_id,
                                                   manager_id)
                                VALUES (%s, %s, %s, %s, %s, %s)
                                ON CONFLICT (team_id) DO NOTHING;
                            """, (row['away_team']['away_team_id'],
                                  row['away_team']['away_team_name'],
                                  row['away_team']['away_team_gender'],
                                  row['away_team']['away_team_group'],
                                  row['away_team']['country']['id'],
                                  manager['id']))
                except KeyError:
                    pass
                conn.commit()

                # stadiums
                try:
                    cur.execute("""
                        INSERT INTO stadiums (stadium_id, stadium_name, country_id) 
                        VALUES (%s, %s, %s)
                        ON CONFLICT (stadium_id) DO NOTHING;
                    """, (row['stadium']['id'],
                          row['stadium']['name'],
                          row['stadium']['country']['id']))
                except KeyError:
                    pass
                conn.commit()

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
                                         match_week,
                                         competition_stage_id,
                                         stadium_id,
                                         referee_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (row['match_id'],
                      row['match_date'],
                      row['kick_off'],
                      row['competition']['competition_id'],
                      row['season']['season_id'],
                      row['home_team']['home_team_id'],
                      row['away_team']['away_team_id'],
                      row['home_score'],
                      row['away_score'],
                      row.get('match_week', None),
                      row.get('competition_stage', {}).get('id', None),
                      row.get('stadium', {}).get('id', None),
                      row.get('referee', {}).get('id', None)))

        # Make the changes to the database persistent
        conn.commit()
        conn.close()
