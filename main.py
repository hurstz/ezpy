import os
from locfunc import *

load_env() # load .env variables
globals().update(os.environ) # globalize .env variables

def main():
    print(TEST_VAR) # access .env variables directly
    fn_name_1(SOME_VAR) # use functions from locfunc
    other_function(OTHER_VAR) # another example
    third_function() # function with no argument

if __name__ == '__main__':
    main()
