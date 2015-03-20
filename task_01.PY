#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" task_01 build a Fibonacci sequence generator function"""


def fibonacci(maxint):
    """function fibonacci that takes one required parameter and return
    args:
        maxint(int): an integer that will serve as the upper bound of the loop
    return:
        Return the newly generated sequence as a list.
    examples:
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """
    
    fibona = []
    counter, fab = 0, 1
    while counter < maxint:
        fibona.append(counter)
        counter, fab = fab, counter + fab
    return fibona
