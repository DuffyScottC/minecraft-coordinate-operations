from distutils.spawn import spawn
import numpy as np
from itertools import chain, combinations


spawners = [
        np.array([0,0,0]),
        np.array([40,3,10]),
        np.array([50,3,30]),
        np.array([60,5,20])
    ]

#2:
#set of all midpoints involving two or more of the points in spawnsers
all_midpoints = {}

def powerset(a_list: list):
    "powerset([1,2,3]) --> (1,2) (1,3) (2,3) (1,2,3)"
    return list(chain.from_iterable(combinations(a_list, r) for r in range(2, len(a_list)+1)))

print(powerset(['a', 'b', 'c', 'd']))