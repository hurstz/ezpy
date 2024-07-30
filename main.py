import os
from locfunc import *

load_env()

def main():
    # access .env variables with os.getenv('<name>')
    print(os.getenv('TEST_VAR'))
    # use functions from locfunc
    fn_name_1(os.getenv('SOME_VAR'))
    fn_name_2()

if __name__ == '__main__':
    main()
