
from sympy.combinatorics import Permutation

p = Permutation([0, 2, 3, 1])

# normal mapping
{i: p(i) for i in range(p.size)}
#{0: 0, 1: 2, 2: 3, 3: 1}

#reverse mapping
{p(i): i for i in range(p.size)}
#{0: 0, 1: 3, 2: 1, 3: 2}


