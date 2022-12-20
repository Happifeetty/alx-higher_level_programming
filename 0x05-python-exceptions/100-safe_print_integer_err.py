#!/usr/bin/python3
safe_print_integer_err(value): 
   from sys import stderr
   try:
       print("{:d}".format(value))

    except Exception as err:
        print("Exception : {:s}".format(str(e)),rfile=stderr)
        return (False)
    else:
        return (True)
