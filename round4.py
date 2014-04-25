"""The cat in some hat.
Given a list of words, create a single list of all of the unique combinations
of those words. This list should be "grouped" by the parent word in
alphabetical order, IE - all combinations of cat, followed by hat, followed by
in, etc etc.
"""
from itertools import permutations, chain

input = ['the', 'cat', 'in', 'some', 'hat']

output = list(chain(*[sorted(''.join(p) for p in permutations(w)) for w in sorted(input)]))

expected = ['act', 'atc', 'cat', 'cta', 'tac', 'tca', 'aht', 'ath', 'hat', 'hta', 'tah', 'tha', 'in', 'ni', 'emos', 'emso', 'eoms', 'eosm', 'esmo', 'esom', 'meos', 'meso', 'moes', 'mose', 'mseo', 'msoe', 'oems', 'oesm', 'omes', 'omse', 'osem', 'osme', 'semo', 'seom', 'smeo', 'smoe', 'soem', 'some', 'eht', 'eth', 'het', 'hte', 'teh', 'the']

assert(output == expected)
