# this file is purely for resetting the entire database

# python3 loader.py

import os

os.system('python3 Loader/dbInit.py && python3 Loader/competitionLoader.py && ' +
          'python3 Loader/matchesLoader.py && python3 Loader/lineupsLoader.py && ' +
          'python3 Loader/eventsLoader.py')
