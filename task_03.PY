#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" task_03.py fuction that returns the max, min and avg words per line"""


# import standard libs
from decimal import Decimal


def lexicographics(to_analyze):
    """a function that takes one parameter return the max, min and avg
       words per line

    args:
        to_analyze(string): a string that will be used to determine the max,min
                            and avg of the word per line
    examples:
        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
                                    Hold on to that feeling.''')
        (5, 3, Decimal(4.0))

        >>> import task_03
        >>> import data
        >>> task_03.lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """

    firstsplit = to_analyze.split('\n')

    linelength = []

    for item in firstsplit:

        split2 = item.split()
        linelength.append(len(split2))

    totallength = len(firstsplit)
    maxa = max(linelength)
    mini = min(linelength)
    total = sum(linelength)
    average = total/Decimal(totallength)

    return (maxa, mini, average)
