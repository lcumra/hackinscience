# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:02:49 2015

@author: pippo
"""

import string
import itertools
from master_mind import *

colors = ""
code = ""
lungo = 0

def gen_colors(x):
    if x in range(0, 26):
        lungo = x
        return alpha[:x]
    else:
        lungo = 26
        return alpha


def gen_code(x, alpha):
    return ''.join(random.choice(alpha[:x]) for i in range(x))


def solve_mind(x, y):
    tries = list(itertools.combinations_with_replacement(list(y), x))
    for i in tries:
        i = "".join(i)
    for j in range(0, len(tries)):
        a = random.choice(tries)
        if a == code:
            return (a, j)
        else:
            culo = master_mind.score_guess(a, code)
            aaa = list(a)
            giusti = itertools.permutations(range(0, lungo), )
        return


def solve_mind(x, y):
    return (x, 2)