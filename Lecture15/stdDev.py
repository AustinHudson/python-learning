def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')

    lengths = [len(l) for l in L]
    mean = float(sum(lengths)) / len(L)
    return (float(sum([(l - mean)**2 for l in lengths]))/len(L))**0.5


L1 = ['a', 'z', 'p']
L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L1)
print stdDevOfLengths(L2)
