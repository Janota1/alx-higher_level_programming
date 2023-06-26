#!/usr/bin/python3
def magic_calculation(e, d):
    result = 0
    for i in range(1, 3):
        try:
            if(i > d):
                raise Exception('Too far')
            else:
                result += d ** e / i
        except:
            result = e + d
            break
    return result
