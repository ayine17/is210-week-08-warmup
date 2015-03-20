#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_02 week 8 warmup"""


def bool_to_str(bval):
    """a function named 'bool_to_str' that takes one required argument:
    args:
        bval(boolean): a boolean or boolean-like value that will be evaluated
                       for truthiness or falsiness

    return:
        return the string, 'Yes' otherwise, return the string 'No'

    example:
        >>> import task_02
        >>> task_02.bool_to_str(True)
        'Yes'

        >>> import task_02
        >>> task 02.bool_to_str('')
        'No

    """
    if bval:
        ans = 'Yes'
    else:
        ans = 'No'
    return ans
