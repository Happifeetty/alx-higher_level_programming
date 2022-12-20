#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))

    except Exception as err:
        print("Exception: {:s}".format(str(e)), file=stderr)
        return (False)
    else:
        return (True)
