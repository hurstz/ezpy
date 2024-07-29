import os

from locfunc import *

# directory of this script
dir_path = os.path.dirname(os.path.realpath(__file__))

# path of .env file
env_file = os.path.join(dir_path, '.env')

# check for .env file exists
if os.path.isfile(env_file):
    # read .env file
    with open(env_file, 'r') as file:
        for line in file:
            # handle whitespace, comments, empty lines
            line = line.strip()
            if line and not line.startswith('#'):
                # split key and value
                key, value = line.split('=', 1)
                # set variable
                os.environ[key.strip()] = value.strip()
else:
    # error message and exit if .env file not found
    print("ERROR: No .env file found")
    exit(1)

# import all the environment variables with .env names
globals().update(os.environ)

# imported function directly accessing .env variable
fn_name_1(SOME_VAR)
fn_name_2()