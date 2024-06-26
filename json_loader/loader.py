# this file is purely for resetting the entire database

# python3 loader.py

import os

os.system('python3 json_loader/dbInit.py && python3 json_loader/competitionLoader.py && ' +
          'python3 json_loader/matchesLoader.py && python3 json_loader/lineupsLoader.py && ' +
          'python3 json_loader/eventsLoader.py')

# create pg_dump
os.system('pg_dump --dbname=project_database --file=dbexport.sql --if-exists --clean')
# make sure analyze is run on all tables - as recommended by postgresql documentation
#  removed due to lack of clarity if modifying dbexport.sql is allowed
# os.system('cat json_loader/sqlInit/analyze.sql >> dbexport.sql')
