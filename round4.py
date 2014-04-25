"""The cat in some hat.
Given a list of words, create a single list of all of the unique combinations
of those words. This list should be "grouped" by the parent word in
alphabetical order, IE - all combinations of cat, followed by hat, followed by
in, etc etc.
"""

input = ['the', 'cat', 'in', 'some', 'hat']

import itertools
output = [word for word in
    reduce(lambda l,l2: l+l2,
           [
              [''.join(c) for c in sorted(itertools.permutations(x))]
              for x in sorted(input)
           ],
           []
    )
]

expected = ['act', 'atc', 'cat', 'cta', 'tac', 'tca', 'aht', 'ath', 'hat', 'hta', 'tah', 'tha', 'in', 'ni', 'emos', 'emso', 'eoms', 'eosm', 'esmo', 'esom', 'meos', 'meso', 'moes', 'mose', 'mseo', 'msoe', 'oems', 'oesm', 'omes', 'omse', 'osem', 'osme', 'semo', 'seom', 'smeo', 'smoe', 'soem', 'some', 'eht', 'eth', 'het', 'hte', 'teh', 'the']

assert(output == expected)
