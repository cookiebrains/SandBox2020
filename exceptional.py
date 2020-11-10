import sys

DIGIT_Map = {
    'zero' :   '0',
    'one':    '1',
    'two':    '2',
    'three':  '3',
    'four':   '4',
    'five':   '5',
    'six':    '6',
    'seven':  '7',
    'eight':  '8',
    'nine':   '9',  
}

def convert(s):
    """Convert a string to an integer."""

    try:
        number = ''
        for token in s:
            number += DIGIT_Map[token]
        return int(number)

    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}",
            file=sys.stderr)
        return -1

from math import log
def string_log(s):
    v = convert(s)
    return log(v)

