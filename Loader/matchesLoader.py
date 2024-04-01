import psycopg
import os
import json

pwd = "Turnbull01!"

# assumes the data location

#with open('D:\COMP3005Final\open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches', 'r') as file:
with psycopg.connect(f"dbname=comp3005finalproject user=postgres password={pwd}") as conn:
    with conn.cursor() as cur:
        directory = os.listdir("D:\COMP3005Final\open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches")
        print(directory)
        
        for dir in directory:
            matchesList = os.listdir('D:\COMP3005Final\open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches/'+dir)
            
            for match in matchesList:
                with open('D:\COMP3005Final\open-data-0067cae166a56aa80b2ef18f61e16158d6a7359a/data/matches/'+dir+'/'+match, 'r') as file:
                    matchjson = json.load(file)
                
                print("yo")
                for row in matchjson:
                    print(row)
                input()
