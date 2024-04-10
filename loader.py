# this file is purely for resetting the entire database

# python3 loader.py

import os

os.system('python3 json_loader/dbInit.py && python3 json_loader/competitionLoader.py && ' +
          'python3 json_loader/matchesLoader.py && python3 json_loader/lineupsLoader.py && ' +
          'python3 json_loader/eventsLoader.py')
