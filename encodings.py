def n_possible_values(nbits: int):
    return 2 ** nbits

print(n_possible_values(4))

from math import ceil, log

def n_bits_required(nvalues):
    return ceil(log(nvalues)/log(2))

print(n_bits_required(256))

print(int("11", base = 8))