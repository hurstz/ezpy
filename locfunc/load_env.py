import os

def load_env():
    """
    Reads the .env file from the same directory as the main script and sets environment variables.
    """
    # Subdirectory of where we expect the .env file to be
    main_script_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one level to the parent directory of the locfunc package
    project_root = os.path.dirname(main_script_dir)

    # Path of .env file
    env_file = os.path.join(project_root, '.env') # */ezpy/.env

    # Check if .env file exists
    if os.path.isfile(env_file):
        # Read .env file
        with open(env_file, 'r') as file:
            for line in file:
                # Handle whitespace, comments, empty lines
                line = line.strip()
                if line and not line.startswith('#'):
                    # Split key and value
                    key, value = line.split('=', 1)
                    # Set environment variable
                    os.environ[key.strip()] = value.strip()
    else:
        # Error message and exit if .env file not found
        print("ERROR: No .env file found")
        exit(1)

    # Import all the environment variables with .env names
    globals().update(os.environ)
