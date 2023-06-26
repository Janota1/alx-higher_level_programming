#!/usr/bin/python3
def safe_print_division(d, e):
    try:
        result = d / e
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
