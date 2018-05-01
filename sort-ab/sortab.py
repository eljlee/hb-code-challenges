"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    sorted_lst = []

    ai = 0
    bi = 0

    while ai<len(a) and bi<len(b):
        if a[ai] < b[bi]:
            sorted_lst.append(a[ai])
            ai += 1
        else:
            sorted_lst.append(b[bi])
            bi += 1

    sorted_lst.extend(a[ai:])
    sorted_lst.extend(b[bi:])
    return sorted_lst

    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
